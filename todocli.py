import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()

app = typer.Typer()

@app.command(short_help='adds an item')
def add(task: str , category: str):
    typer.echo(f"adding {task} , {category}")

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")


