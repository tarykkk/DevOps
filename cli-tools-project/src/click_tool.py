#!/usr/bin/env python3
"""
CLI tool using Click library.
Validates and prints names that don't start with 'p' or 'P'.
"""

import click


@click.group()
def cli():
    """CLI tool for name validation and printing."""
    pass


@cli.command()
@click.option('--name', required=True, help='Name to print (must not start with p/P)')
def say(name):
    """
    Print the name if it doesn't start with 'p' or 'P'.
    
    Examples:
        python click_tool.py say --name Alice
        python click_tool.py say --name John
    """
    if name and name[0].lower() == 'p':
        click.echo("Ім'я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()