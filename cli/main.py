#!/usr/bin/env python

"""
Main cli or app entry point

"""

import click


@click.group()
def cli():
    """Main entry point for the cli"""
    pass


@cli.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers together

    Example:
        cli add 1 2
    """

    click.echo(click.style(str(a + b), fg="green"))


def add_two(a: int):
    """Add two to a number"""
    return a + 2


def add_three(a: int):
    """Add three to a number"""
    return a + 3


# write a click cli method that takes in a number and adds 2 to it
@cli.command("add_two")
@click.argument("a", type=int)
def add_two_cli(a):
    """Add two to a number

    Example:
        cli add_two 1
    """

    click.echo(click.style(str(add_two(a)), fg="green"))
