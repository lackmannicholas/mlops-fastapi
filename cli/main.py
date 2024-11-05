#!/usr/bin/env python

"""
Main cli or app entry point

"""

import click
from nlp.text_generator import TextGenerator


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


# write a click cli method for nlp.text_generator.TextGenerator.generate_text
@cli.command("generate_text")
@click.argument("text", type=str)
@click.option(
    "--num_sentences", type=int, default=1, help="Number of sentences to generate"
)
@click.option(
    "--model", type=str, default="gpt2", help="Model to use for text generation"
)
def generate_text_cli(text, num_sentences, model):
    """Generate text based off of a short string

    Example:
        mlops-cli generate_text "Once upon a time" 10
    """
    generator = TextGenerator(model)
    click.echo(
        click.style(
            str(generator.generate_text(text, num_sentences).get("generated_text")),
            fg="green",
        )
    )
