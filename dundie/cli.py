"""Cli functions"""
import json

import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dundie Mifflin Rewards System

    This cli application cotrols DM Rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database

    ## Features
    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Dundie Mifflin Associates")
    headers = ["email", "name", "dept", "role", "created"]
    for header in headers:
        table.add_column(header, style="magenta")

    result = core.load(filepath)
    for person in result:
        values = [str(value) for value in person.values()]
        table.add_row(*values)

    console = Console()
    console.print(table)


@main.command()
@click.option("--output", required=False)
@click.option("--dept", required=False)
@click.option("--email", required=False)
def show(output, **query):
    """Shows information about user"""
    result = core.read(**query)
    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))

    if not result:
        print("Nothing to show")

    table = Table(title="Dundie Mifflin Associates")
    for key in result[0]:
        table.add_column(key.title(), style="magenta")

    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    """Add points to the user or dept."""
    core.add(value, **query)
    ctx.invoke(show, **query)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
def remove(ctx, value, **query):
    """Remove points to the user or dept"""
    core.add(-value, **query)
    ctx.invoke(show, **query)
