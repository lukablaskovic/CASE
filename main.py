import asyncio
from functools import wraps

import os
import json
import typer
from typing_extensions import Annotated

from rich.console import Console
from rich.spinner import Spinner
from rich.markdown import Markdown
from rich import print

from educoder import educoder_fetch, educoder_fetch_exam_solutions, print_json, extract_code_from_solutions, solutions_extracted
from evaluator import call_evaluator
from helpers.file_operations import read_file_content

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

def concatenate_js_code(json_data):
    data_dict = json.loads(json_data) 
    code_snippets = data_dict.get('code_snippets', [])
    return '\n\n'.join([snippet['js_code'] for snippet in code_snippets if 'js_code' in snippet and snippet['js_code'].strip()])

async def evaluate_solutions(code_folder, exam):
    instructions = read_file_content("instructions.txt")
    tasks_text = read_file_content("text_a_new_hope.txt")
    
    for filename in os.listdir(code_folder):
        if filename.startswith('js_code') and filename.endswith('.json'):
            filepath = os.path.join(code_folder, filename)
            json_data = read_file_content(filepath)
            student_code = concatenate_js_code(json_data)
            

            student_email = filename[len('js_code_'):-len('.json')]

            await call_evaluator(instructions=instructions, tasks_text=tasks_text, student_code=student_code, student_email=student_email, exam_password=exam)


@default_app.command()
@typer_async
async def evaluate(exam: str):
    code_folder = f"exams/{exam}/code_solutions"
    if not solutions_extracted(exam):
        console.print("Exam solutions not extracted or no solutions available. Please run the 'educoder extract-solutions' command first.")
        return         
    print(f"Evaluating solutions for exam '{exam}'...")
    await evaluate_solutions(code_folder, exam)



@default_app.command()
def test(username: str):
    typer.echo(f"User {username} logged in")

if __name__ == "__main__":
    typer.run(app())