import typer
from typing_extensions import Annotated
from educoder import educoder_fetch, educoder_fetch_exam_solutions, print_json
from rich.console import Console
from rich.spinner import Spinner
from rich.markdown import Markdown
from rich import print

app = typer.Typer()
console = Console()

educoder_connector = typer.Typer()
app.add_typer(educoder_connector, name="educoder")

default_app = typer.Typer()
app.add_typer(default_app, name="")

def description():
    description = """
# CASE - Coding Assessment & Scoring Engine

CASE is a powerful CLI tool which helps you evaluate and score coding assessments. 
It is designed to work with 💻**EduCoder**, a platform for creating and managing coding assessments, but you can also use it manually.

- Fetch data from 💻EduCoder
- Fetch exam solutions
- Evaluate and score coding assessments using GPT-4
- Generate reports and insights
- Export data to Google Sheets

Enjoy the **rich** experience!
    """
    md = Markdown(description)
    console.print(md)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Welcome to My Fancy CLI.
    """
    if ctx.invoked_subcommand is None:
        description()

# EduCoder commands

@educoder_connector.command()
def fetch(collection: Annotated[str, typer.Argument(help="Firebase collection to fetch from.")] = "exams", printall: Annotated[bool, typer.Option(help="Print the fetched data in CLI.")] = False):
    
    with console.status("Fetching from 💻 EduCoder...", spinner="dots"):
        docs = educoder_fetch(collection=collection)
    
    if printall:
        typer.echo(f"✏️  Printing '{collection}' collection...")
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
def solutions(exam: Annotated[str, typer.Argument(help="Enter exam code")],
              student: Annotated[str, typer.Argument(help="Enter student email", rich_help_panel="Optional arguments")] = "",
              save: Annotated[bool, typer.Option(help="Save the fetched data.")] = False):
    filepath = f"exams/{exam}" # Firebase Storage path
    with console.status("Fetching exam solutions from 💻 EduCoder...", spinner = "dots"):
        data = educoder_fetch_exam_solutions(filepath, student=student, save = save)

    if (data):
        print(data)


@default_app.command()
def test(username: str):
    typer.echo(f"User {username} logged in")


if __name__ == "__main__":
    app()
