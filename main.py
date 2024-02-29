import typer
from typing_extensions import Annotated
from educoder import educoder_fetch, educoder_fetch_exam_solutions, print_json
from rich.console import Console
from rich.spinner import Spinner


app = typer.Typer()
console = Console()

educoder_connector = typer.Typer()
app.add_typer(educoder_connector, name="educoder")

default_app = typer.Typer()
app.add_typer(default_app, name="")

# EduCoder commands

@educoder_connector.command()
def fetch(collection: Annotated[str, typer.Argument(help="Firebase collection to fetch from.")] = "exams", printall: Annotated[bool, typer.Option(help="Print the fetched data in CLI.")] = False):
    
    with console.status("Fetching from 💻 EduCoder...", spinner = "dots"):
        docs = educoder_fetch(collection=collection)
    if printall:
        typer.echo(f"✏️  Printing '{collection}' collection...")
        print_json(docs)

@educoder_connector.command()
def solutions(exam: Annotated[str, typer.Argument(help="Enter exam code")],
              student: Annotated[str, typer.Argument(help="Enter student email", rich_help_panel="Optional arguments")] = "",
              save: Annotated[bool, typer.Option(help="Save the fetched data.")] = False):
    filepath = f"exams/{exam}"
    with console.status("Fetching exam solutions from 💻 EduCoder...", spinner = "dots"):
        data = educoder_fetch_exam_solutions(filepath, student=student, save = save)
    typer.echo(data)

@default_app.command()
def test(username: str):
    typer.echo(f"User {username} logged in")


if __name__ == "__main__":
    app()
