"""Perform integer squaring with different approaches."""

# TODO: resolve all of the TODO markers in this file
# TODO: ensure that your build is passing in GitHub actions
# TODO: read the instructions in the README.md file for an overview
# TODO: read the instructions on the course web site for all details
# TODO: delete all of the TODO markers and either rewrite or delete all comments

from enum import Enum
from pathlib import Path
from typing import Callable
from typing import List

import typer
from rich.console import Console

# TODO: create a Typer object with the name cli to support the command-line interface
# by typing `cli = typer.Typer()`
# If you want to learn more, read this intro to Typer
# https://medium.com/@HeCanThink/typer-building-clis-in-python-%EF%B8%8F-8f496d295d1c


class IntegerSquareApproach(str, Enum):
    """Define the name of the approach to squaring a number."""

    FOR_LOOP = "for"
    WHILE_LOOP = "while"


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # TODO: determine if the file is not None and if it is a file
    # TODO: determine if the file is valid
    # TODO: return the final verdict about the file


def compute_square_while(value: int) -> int:
    """Compute the square of a number through iteration with a while loop."""
    # TODO: initialize the number of iterations and the answer
    # TODO: repeatedly increase the answer until getting to the value
    # TODO: return the computed integer square using a while loop


def compute_square_for(value: int) -> int:
    """Compute the square of a number through iteration with a for loop."""
    # TODO: initialize the answer to zero
    # TODO: repeatedly add to the answer the absolute value of the variable called value
    # TODO: return the computed integer square


def compute_square_iterative(
    contents: str, square_function: Callable[[int], int]
) -> List[int]:
    """Compute the square of all of the integer values inside of the contents."""
    # TODO: create an empty list for the squared values by typing `list_of_squared_vals: List[int] = []`
    # TODO: split the contents variable into lines using .split by typing `split_contents = contents.split("\n")`
    # iterate through all of the lines in the split contents
    for line in split_contents:
        try:
            # TODO: convert the line into a number by typing `number = int(line)`
            # TODO: perform the number squaring computation with square_function by typing `number_squared = square_function(number)`
            # TODO: add the squared_number to the square_list by typing `list_of_squared_vals.append(num_squared)`
        except ValueError:
            pass
    # TODO: return the list of the squared numbers by typing `return list_of_squared_vals`


@cli.command()
def square(
    approach: IntegerSquareApproach = IntegerSquareApproach.FOR_LOOP,
    directory: Path = typer.Option(None),
    file: Path = typer.Option(None),
) -> None:
    """Provide a command-line interface for iteratively squaring all integers in a file."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    file_fully_qualified = directory / file
    # display a message to explain the file that will be input
    console.print(f":smiley: Squaring numbers in a file called {file_fully_qualified}!")
    console.print()
    # the file is value and so the program should search through it for the word
    if confirm_valid_file(file_fully_qualified):
        # read in the contents of the file
        contents_text = file_fully_qualified.read_text()
        square_list = []
        # the for loop approach should be invoked
        if approach.value == IntegerSquareApproach.FOR_LOOP:
            # specify the square function to be compute_square_for
            square_function = compute_square_for
        # the while loop approach should be invoked
        elif approach.value == IntegerSquareApproach.WHILE_LOOP:
            # specify the square function to be compute_square_while
            square_function = compute_square_while
        # call the compute_square_iterative function with:
        # --> the contents_text variable with the numerical values as text
        # --> the square function that is set to be the square function
        square_list = compute_square_iterative(contents_text, square_function)
        # display the list of squared values
        console.print(square_list)
    # the file was not valid and thus you cannot perform the number squaring
    else:
        console.print(
            f":person_shrugging: {file_fully_qualified} was not a valid file! Sorry, cannot square the numbers!"
        )
        console.print()
