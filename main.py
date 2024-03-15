import asyncio
from functools import wraps

import os
import subprocess
import json
import typer
from typing_extensions import Annotated

from rich.console import Console
from rich.spinner import Spinner
from rich.markdown import Markdown
from rich import print

from educoder import educoder_fetch, educoder_fetch_exam_solutions, print_json, extract_code_from_solutions, solutions_extracted
from evaluator import call_evaluator
from helpers.file_operations import read_file_content, export_dict_to_csv
import pypandoc

app = typer.Typer()
console = Console()

educoder_connector = typer.Typer()
app.add_typer(educoder_connector, name="educoder", help="Commands to interact with 💻 EduCoder")

default_app = typer.Typer()
app.add_typer(default_app, name="CASE", help="CASE - Coding Assessment & Scoring Engine")

def typer_async(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper

def description():
    description = """
# CASE - Coding Assessment & Scoring Engine

**CASE** is a powerful CLI tool which helps you evaluate and score coding assessments. 
It is designed to work with 💻 **EduCoder**, a platform for creating and managing coding assessments, but you can also use it manually.

- Fetch data from 💻 EduCoder
- Fetch exam solutions from 💻 EduCoder
- Evaluate and score coding assessments using GPT-4
- Define custom scoring rubrics
- Generate reports and insights
- Many data export options
    """
    md = Markdown(description)
    console.print(md)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    CASE is a powerful CLI tool which helps you evaluate and score coding assessments. It is designed to work with 💻 EduCoder, a platform for creating and managing coding assessments, but you can also use it manually.
    """
    if ctx.invoked_subcommand is None:
        description()

# EduCoder commands

@educoder_connector.command()
def get_docs(collection: Annotated[str, typer.Argument(help="Firebase collection to fetch from.")] = "exams", printall: Annotated[bool, typer.Option(help="Print the fetched data in CLI.")] = False):
    """
    Fetch Firestore documents from 💻 EduCoder. COLLECTION defaults to exams.
    """
    with console.status("Fetching from 💻 EduCoder...", spinner="dots"):
        docs = educoder_fetch(collection=collection)
    
    if printall:
        typer.echo(f"🖨️  Printing '{collection}' collection...")
        print_json(docs)
    else:
        num_docs = len(docs)
        typer.echo(f"✅ Fetched {num_docs} documents from '{collection}' collection.")
        if num_docs > 0:
            sample_docs = docs[:5] 
            typer.echo("Sample document IDs:")
            for doc in sample_docs:
                typer.echo(f"- {doc.get('id', 'No ID')}") 


@educoder_connector.command()
def get_solutions(exam: Annotated[str, typer.Argument(help="Enter exam code")],
              student: Annotated[str, typer.Argument(help="Enter student email", rich_help_panel="Optional arguments")] = "",
              save: Annotated[bool, typer.Option(help="Saves the fetched data")] = False):
    """
    Pull exam solutions from 💻 EduCoder. EXAM argument is required.
    """
    filepath = f"exams/{exam}" # Firebase Storage path
    with console.status("Fetching exam solutions from 💻 EduCoder...", spinner = "dots"):
        data = educoder_fetch_exam_solutions(filepath, student=student, save = save)
    
    if (data):
        typer.echo(f"🖨️  Printing '{exam}' solutions...")
        print(data)

@educoder_connector.command()
def extract_solutions(exam: Annotated[str, typer.Argument(help="Enter exam code")],
                    js: Annotated[bool, typer.Option(help="Extract JavaScript code from exam solutions")] = False,
                    html: Annotated[bool, typer.Option(help="Extract HTML code from exam solutions")] = False):
    """
    Extract JavaScript code from exam solutions. EXAM argument is required.
    """
    exam_folder = f"exams/{exam}"
    
    if not os.path.exists(exam_folder):
        print(f"The folder '{exam_folder}' does not exist. Please re-check the EXAM code or pull the solutions first using: 'get-solutions EXAM --save.")
        return
    
    if (not html and not js):
        js = True # Default to JavaScript if no option is provided
    result = extract_code_from_solutions(exam_folder, js, html)
    print(result)
    
def to_js_markdown(json_data, json_response):
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    markdown_output = ""

    for i, snippet in enumerate(data.get('code_snippets', []), start=1):
        js_code = snippet.get('js_code', '')
        task_key = f'task_{i}'
        task_points = json_response.get(task_key, 'N/A')

        markdown_output += f"#### Zadatak {i}\n"
        markdown_output += "```javascript\n"
        markdown_output += f"{js_code}\n"
        markdown_output += "```\n"
        markdown_output += f"- **Bodovi**: {task_points}\n\n"

    return markdown_output

async def evaluate_solution(filepath, instructions, tasks_text, exam):
    json_data = read_file_content(filepath)
    student_email = os.path.basename(filepath).replace('js_code_', '').replace('.json', '')


    json_response = await call_evaluator(
        instructions=instructions,
        tasks_text=tasks_text,
        student_code=json_data, 
        student_email=student_email,
        exam_password=exam
    ) 

    return student_email, json_data, json_response


async def evaluate_solutions(code_folder, exam):
    instructions = read_file_content("instructions.txt")
    tasks_text = read_file_content("exam_texts/text_2jMJ4dU.txt")

    markdown_content = f"# Exam Tasks\n\n{tasks_text}\n\n"
    total_cost_exam = 0
    all_responses = [] 

    filepaths = [
        os.path.join(code_folder, filename)
        for filename in os.listdir(code_folder)
        if filename.startswith('js_code') and filename.endswith('.json')
    ]

    evaluations = await asyncio.gather(*[
        evaluate_solution(filepath, instructions, tasks_text, exam)
        for filepath in filepaths
    ])

    print("all evaluations", evaluations)

    for student_email, student_code, json_response in evaluations:
        print(f"Creating report for {student_email}...")
        total_cost_exam += json_response.get('total_cost', 0)
        all_responses.append(json_response)

        markdown_content += f"## {student_email}\n\n### Rješenje studenta\n"
        markdown_content += to_js_markdown(student_code, json_response)
        markdown_content += f"\n## Evaluacija\n\n- **Ukupno bodova**: {json_response.get('total_points', 'N/A')}\n"
        markdown_content += f"- **Feedback**: {json_response['feedback']}\n"
        markdown_content += f"- **Cijena evaluacije**: ${json_response.get('total_cost', 0):.2f}\n\n"

    markdown_content += f"\n\n# Ukupna cijena evaluacije ispita {exam}: ${total_cost_exam:.2f}\n"

    markdown_file = f"reports/{exam}_report.md"
    with open(markdown_file, 'w', encoding="utf-8") as file:
        file.write(markdown_content)
        
    """
    pdf_file = f"reports/{exam}_report.pdf"
    pypandoc.convert_file(markdown_file, 'pdf', outputfile=pdf_file)

    print(f"PDF report generated: {pdf_file}")
    """
    output_dir = f"results/{exam}/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = f"{output_dir}evaluations.csv"
    export_dict_to_csv(all_responses, output_file)

    print(f"All evaluations exported to CSV: {output_file}")

@default_app.command()
@typer_async
async def evaluate(exam: str, pdf: Annotated[bool, typer.Option(help="Generate PDF report")] = False):
    code_folder = f"exams/{exam}/code_solutions"
    if not solutions_extracted(exam):
        console.print("Exam solutions not extracted or no solutions available. Please run the 'educoder extract-solutions' command first.")
        return         
    print(f"Evaluating solutions for exam '{exam}'...")
    await evaluate_solutions(code_folder, exam)

if __name__ == "__main__":
    typer.run(app())
    


# How to use with EduCoder?
# 1. python main.py educoder get-solutions EXAM --save
# 2. python main.py educoder extract-solutions EXAM --js
# 3. python main.py evaluate EXAM --pdf