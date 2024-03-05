import os
import typer
from typing_extensions import Annotated
from educoder import educoder_fetch, educoder_fetch_exam_solutions, print_json, extract_code_from_solutions, solutions_extracted
from rich.console import Console
from rich.spinner import Spinner
from rich.markdown import Markdown
from rich import print

app = typer.Typer()
console = Console()

educoder_connector = typer.Typer()
app.add_typer(educoder_connector, name="educoder", help="Commands to interact with 💻 EduCoder")

default_app = typer.Typer()
app.add_typer(default_app, name="CASE", help="CASE - Coding Assessment & Scoring Engine")

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

@default_app.command()
def evaluate(exam: str):
    if (not solutions_extracted(exam)):
        typer.echo("Exam solutions not extracted. Please run the 'extract-solutions' command first.")
        return
    typer.echo(f"Evaluating solutions for exam '{exam}'")
    
    

@default_app.command()
def test(username: str):
    typer.echo(f"User {username} logged in")

if __name__ == "__main__":
    app()
