# Integer Squaring Engineering Lab

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

In this lab, you job is to implement python source code to generate a Command
Line Interface (CLI) which squares numbers stored in a file in two ways. The
first way that the CLI will square numbers is by adding repeatedly in a for
loop. The second way that the CLI will square numbers is by adding repeatedly
in a while loop. Since all the numbers for squaring are stored in the file, your
code will also have to be able to read in a file, retrieve the numbers, and
pass numbers into the appropriate squaring algorithms.

This lab is an Engineering Lab. As described in the syllabus:

**Engineering Labs** are graded, i.e. assigned a number or percentage
indicative of the proportion of points earned relative to the total possible.

- Fifty percent of the grade of each Engineering Lab is determined by
  the percentage of gatorgrade checks passed.
- One quarter of the grade is determined by code correctness following a rubric.
- One quarter of the grade is determined by professional skills and presentation
  following a rubric. Professional presentation is impacted by linting,
  formatting, testing, profiling, duplication avoidance, commenting, markdown
  styling and communication in reflections.

## Learning Objectives

1. Use Git and GitHub to manage source code file changes
2. Use the poetry virtual environment tools and helper tasks to link and format
   both code and markdown
3. Do detective work to figure out how the functions work together
4. Implement algorithms to square numbers
5. Use code for accessing files
6. Write clearly about the coding and development concepts in this assignment.

## Quick Links

- Due date: Check Discord or the
  [Course Materials Schedule](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials/blob/main/Schedule.md)
- Policy on
  [Tokens](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#tokens)
- [Token Form for Automatic Extension](https://forms.gle/y9Mz55hQKr84wzvXA)
- Policy for
  [Assignment Evaluation](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-evaluation)
- Policy for [Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-submission).
- [#data-structures Discord channel](https://discord.com/channels/877320365825749002/1274744318124359732)
- [Starter repo](https://github.com/allegheny-college-cmpsc-101-fall-2024/integer-squaring-starter)

## Policy Reminders

Students are reminded to uphold the Honor Code. Cloning this assignment
repository is a commitment to the latter.

For this assignment, you may use class materials, the textbook, notes,
and the internet, including AI, for reference and learning. AI may **not** be
used to generate answers that you submit. All code and writing that are turned
in **must be your own work and your own words**. Copying or otherwise
representing ChatGTP or other AI outputs as your own work or your own words is
not permitted.

Please ask questions freely in Lab, on the #data-structures Discord channel,
TL office hours, instructor office hours, or by opening a GitHub Issue with
@emgraber tagged at least 24 hours before the deadline.

Modifications to the gatorgrade.yml file are not permitted without explicit
instruction.

## Project Details ([Project Overview](#project-overview) Below)

### Goals

This engineering lab invites you to combine what you learned about the basics
of Python programming to implement a useful program that can compute the square
for all of the integer values stored inside of a file. As part of this project
you will learn how to navigate the source code in a Python file, perform file
input and output using `Path` objects from `pathlib`, implement Python
functions, and implement and test functions that contain either a `for` and or
a `while` loops.

### Expected Output

This project invites you to implement a number squaring program called `square`.
You can install the dependencies for the `square` program and ensure that it is
ready to run by using your terminal to type the command `poetry install` in the
`square/` directory that contains the `pyproject.toml` and `poetry.lock` files.
The program can accept as input a file of numbers, a directory that contains the
this file, and the name of an approach to squaring an integer. If you run the
program correctly, it will iterate through the file of numbers, compute the
square for each number, and output a complete list of the squared values. For
instance, if you run the program with the command `poetry run square --approach
for --directory input --file numbers.txt` it produces this output:

```text
😃 Squaring numbers in a file called input/numbers.txt!

[
    5184,
    841,
    3721,
    1764,
    1936,
    ...
]
```

In addition to having a feature that lets you square numbers using a `for` loop,
the `square` program can perform the same task by using a `while` loop! If you
run the program with the command
`poetry run square --approach while --directory input --file numbers.txt`
then the program should produce the same output as given
above this paragraph. If you run the command `poetry run square --help` you
should see the following output that explains how to use the `square` program:

```shell
 Usage: square [OPTIONS]

 Provide a command-line interface for iteratively squaring all integers
 in a file.

╭─ Options ─────────────────────────────────────────────────────────────╮
│ --approach                  [for|while]  [default: for]               │
│ --directory                 PATH         [default: None]              │
│ --file                      PATH         [default: None]              │
│ --install-completion                     Install completion for the   │
│                                          current shell.               │
│ --show-completion                        Show completion for the      │
│                                          current shell, to copy it or │
│                                          customize the installation.  │
│ --help                                   Show this message and exit.  │
╰───────────────────────────────────────────────────────────────────────╯
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add all of the missing features and ensure that `square` produces the
expected output. Once the program is working correctly, you should also try to
use it when specifying a file that is not available on your computer! For instance,
if you run it with the command `poetry run square --approach for --directory input
--file numberswrong.txt` then it will not perform the number squaring and
instead produce the following output:

```shell
😃 Squaring numbers in a file called input/numberswrong.txt!

🤷 input/numberswrong.txt was not a valid file! Sorry, cannot square the
numbers!
```

Don't forget that if you want to run the `square` program you must use your
terminal window to first go into the GitHub repository containing this
project and then go into the `square/` directory that contains the project's
source code. Finally, remember that before running the program you must run
`poetry install` to add the dependencies.

### Adding Functionality

If you study the file `square/square/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `square` will produce correct output. If you run the provided
test suite with the command `poetry run task test` you will see that it produces
output like the following:

```text
================================ ERRORS =================================
_________________ ERROR collecting tests/test_square.py _________________
tests/test_square.py:4: in <module>
    from square import main
square/main.py:54: in <module>
    ???
E   NameError: name 'cli' is not defined
======================== short test summary info ========================
ERROR tests/test_square.py - NameError: name 'cli' is not defined
!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!
=========================== 1 error in 0.14s ============================
```

Alternatively, running the program with a command like `poetry run square
--approach for --directory input --file numbers.txt` will produce the following
output:

```shell
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/gkapfham/.asdf/installs/python/3.10.5/lib/python3.10/
  importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/gkapfham/working/teaching/github-classroom/proactive-programmers/
  data-abstraction/starters/engineering-efforts/integer-squaring-starter/
  square/square/main.py", line 54, in <module>
    @cli.command()
NameError: name 'cli' is not defined
```

This output suggests that the `cli` variable was not correctly defined! After
correctly resolving this issue you should find the other `TODO` markers and
correctly resolve them. For instance, you can add this function to the `main.py`
file:

```python linenums="1"
def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False
```

Line `1` of this function defines the signature of `confirm_valid_file`, showing
that it will take as input a `Path` object and return as output a `bool` to
indicate whether or not the file is valid. Lines `4` through `7` confirm that
the `file` is valid and `True` if it is both not `None` and a valid file.
Alternatively, line `9` returns `False` to indicate that `file` is not valid. In
addition to `confirm_valid_file`, you must also implement these functions:

- `def compute_square_while(value: int) -> int`
- `def compute_square_for(value: int) -> int`
- `def compute_square_iterative(
  contents: str, square_function: Callable[[int], int]) -> List[int]:`

It is worth noting that the `compute_square_iterative` function is a
higher-order function that accepts as one of its inputs the `square_function`
that should be either `compute_square_for` or `compute_square_while`. The person
running the `square` program can pick which of these functions the program will
call by specifying either `for` or `while` as one of the program's command-line
arguments. The `square` program uses the Typer package and the following source
code to ensure that the program only accepts one of these two options. For
instance, if you try to run the program with the command `poetry run square
--approach recursion --directory input --file numbers.txt` it will produce the
following error message because `recursion` is not a valid option:

```text
Usage: square [OPTIONS]
Try 'square --help' for help.
╭─ Error ───────────────────────────────────────────────────────────────╮
│ Invalid value for '--approach': 'recursion' is not one of 'for',      │
│ 'while'.                                                              │
╰───────────────────────────────────────────────────────────────────────╯
```

The `square` program contains the following source code to specify the valid
options:

```python linenums="1"
class IntegerSquareApproach(str, Enum):
    """Define the name of the approach to squaring a number."""

    FOR_LOOP = "for"
    WHILE_LOOP = "while"
```

Line `1` of this code segment defines a new class called `IntegerSquareApproach`
that operates as a enumeration of values. Specifically, an instance of the
`IntegerSquareApproach` will have a `value` variable that is either equal to
`FOR`, designating that the input integer should be squared through iteration
with a `for` loop or equal to `WHILE`, meaning that it should complete the same
task with a `while` loop. The `square` program uses the `IntegerSquareApproach`
to define the acceptable arguments that a person can pass to it through its
command-line interface.

It is possible that you will become overwhelmed by the details associated
with Python programming as you implement all of the required functionality
for the `square` program. If you get stuck on any aspect of this project,
take the time to write out a list of steps that you have already taken, a
summary of what worked and did not work, and the current questions that
you have. After taking these important steps, you can share a status
update and ask questions in the
[#data-structures Discord channel](https://discord.com/channels/877320365825749002/1274744318124359732)

## Running Checks

### Helper Tasks

Helper tasks are run in the terminal with the poetry environment activated.
The format of the commands are always `poetry run task xyz`...where `xyz`
is the helper task name.

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable "helper
task" names like `ruff`, `fix`, `ruffdetails`, etc.

```toml
[tool.taskipy.tasks]
```

If you are in the `square` directory that contains the
`pyproject.toml` file, the helper tasks
make it easy to run commands like `poetry run task ruff` to automatically run
the ruff linter designed to check the Python source code in your program
to confirm that your source code adheres to industry standards for formatting.
You can also use the command `poetry run task fix` to automatically reformat the
source code. `poetry run task ruffdetails` will print out detailed linting errors
that point to exactly what ruff views as a linting error. Make sure to examine
the `pyproject.toml` file for other convenient tasks that you can use to both
check and improve your project!

### Gatorgrade

The command `gatorgrade --config config/gatorgrade.yml` will check your work. If
your work meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. Try to pass as many checks as you can. Missing some checks will only
impact a part of your grade in this Engineering Lab. Note, modifications to the
gatorgrade.yml file are not permitted without explicit instruction.

### Pytest

It is worth noting that the test suite for the `square` program is missing a
test case! You can create the missing test case based on the following example
code.

```python linenums="1"
def test_compute_square_iterative_for_loop():
    """Confirm that the for loop calculates squares correctly for negatives
    and positives in loop."""
    number_list = """-72
        29
        61
        -42
        44"""
    square_function = main.compute_square_for
    square_list = main.compute_square_iterative(number_list, square_function)
    assert square_list == [72 * 72, 29 * 29, 61 * 61, 42 * 42, 44 * 44]
```

This test case takes the following steps:

- Lines `3` through `7`: Create a `number_list` multiple-line
  string with integers for squaring
- Line `8`: Defines the `square_function` to be the `compute_square_for`
  function in `main`
- Line `9`: Calls `compute_square_iterative` with `number_list` and `square_function`
- Line `9`: Stores the output of the `compute_square_iterative` function in `square_list`
- Line `10`: Asserts that the `square_list` variable contains
  the squares of each number

Ultimately, you should write a new test that follows these steps for the
`compute_square_while` function! Finally, please make sure that you explain all
of the steps in these test cases by adding single-line comments to each line in
every test case function.

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented, and answer all of the other questions about your experiences in
completing this project.

## Project Assessment

Since this project is an engineering lab, it is aligned with the
**evaluating** and **creating** levels of [Bloom's
taxonomy](/proactive-learning/blooms-taxonomy/).
You may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
specification. This engineering lab is graded based on the percentage
of the gatorgrade checks passed, and other evaluations described in
the syllabus.

Before you finish all of the deliverables required by this project is worth
pausing to remember that the instructor will give advance feedback to any
Allegheny College learner who requests it through GitHub and Discord at
least 24 hours before a project's due date! Seriously, did you catch that?
This policy means that you can have a thorough understanding of ways to
improve your project **before** its final assessment!
See [Policy Reminders](#policy-reminders) above for instructions.

## Project Overview

Accept the GitHub Classroom Assignment. Then clone the repo following these
step:

- In GitHub, copy the SSH link to your repo from the green `code` button
- Open a terminal
- `cd` to a location where you would like to store the project repo
- type `git clone` then paste in the link
- hit enter, type in passphrase if prompted.

After cloning this repository to your computer, please take the following
steps:

- Use the `cd` command to change into the directory for this repository.
- Specifically, you can change into the program directory by typing `cd square`.
- Install the dependencies for the project by typing `poetry install`.
- Run the program in its two different modes by typing:
  - `poetry run square --approach for --directory input --file numbers.txt`
  - `poetry run square --approach while --directory input --file numbers.txt`
  - Please note that the program will not work unless you add the required
    source code at the designated `TODO` markers.
- Confirm that the program is producing the expected output described
  [above](#expected-output)
- Run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file.

Submit work to GitHub using git:

- Open a terminal
- `cd` to the project directory on your computer
- type `git status` to see a list of files you have updated
- type `git add .` to "stage" your files
- type `git commit -m "WRITE YOUR OWN MESSAGE"` to commit your files
- type `git push origin main` to submit your files
- type your ssh passphrase if requested
