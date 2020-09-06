# Python on steroids

## Story

In your new position you have to do code reviews for junior colleagues.
Their code is rather clumsy and verbose, and don't really use
Python's rich standard library. Your job is to refactor the functions
into a more elegant and readable form.

Luckily, there are tests included along the codebase so you can check
if you have altered the behavior of the refactored functions.

## What are you going to learn?

You'll have to:

- know about and use advanced language features,
- think in terms of density AND readability at the same time,
- refactor code without breaking functionality.

## Tasks

1. Parse a line describing user data in the format: `FirstName LastName usernameexample.com`.
Return a tuple: `(first_name, last_name, user, host)`
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **three lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

2. Compare two lists of file names, and find the files that were removed or added.
Return a dictionary with two keys:
- 'removed': sorted list of removed files
- 'added': sorted list of added files
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **three lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

3. Write out a log line in a specific format.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **two lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

4. Find the biggest rectangle in a sequence.
Rectangles are represented as tuples of `(width, height)`.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **one line** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

5. Find a pattern in file. Print out all lines that match the pattern
(case-insensitive) with line numbers.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **four lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

6. Read all words from a file that are longer than given length.
Convert to lowercase, and remove punctuation.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **three lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

7. Find top `n` words in a file. Return a list of tuples (word, count), ordered by
descending count.
    - Running the program results in the exact same behavior before and after refactoring.
    - The function body is at most **two lines** long (not counting empty and comment lines).
    - The code is more (or at least not less) readable than before the refactoring.

## General requirements

- There are no nasty tricks to reduce actual line numbers like using semicolons (`print(x); print(y); print(z)`), or using dynamic code evaluation tools (`eval` or `exec`).

## Hints

- Run the included doctests by running `python3 -m doctest
  functions.py`, or add the `-v` switch for a more verbose report.
- Try to use the language features linked below in the
  Background materials section.

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/solo/blueprint/python-on-steroids/python).

## Background materials

- [`max`](https://docs.python.org/3/library/functions.html#max) and [`sort`](https://docs.python.org/3/library/stdtypes.html#list.sort) with using the `key` parameter
- [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [sequence packing and unpacking](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate)
- [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#with) (for [reading files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files))
- [string formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting) (f-strings or `.format()`)
- [`collections.Counter()`](https://docs.python.org/3/library/collections.html#collections.Counter)
