"""
This Python challenge will help you to familiarize yourself with
Python's ``random`` module, which is of great help for, well,
doing anything requiring a degree of randomness.

This module includes both instructions for getting started, an area
for your to write your code, and tests to ensure that your code
functions as intended. The tests are automatically run when
you run the module. You are encouraged to look at the tests in order
to understand how they work and what they are testing.

You may use your own functions in other functions, if you desire.

If you haven't seen the type annotation syntax yet, you can find
a description of it here: https://docs.python.org/3/library/typing.html
"""

# # # Place your imports below this line # # #

from inspect import getsource
from sys import argv
from typing import Sequence, Union

import pytest


#
#
#
# # # Coding Challenges Begin # # #
#
#
#


# One: select a random list item
#   For this challenge, use the random module to select a random item
#   from a list. For now, you may only use the ``randint`` function
#   from the random module. You may use any other Python modules, methods,
#   etc.


def random_item_with_randint(some_list: list):
    """Return a random item from the list

    :param some_list: a list of items. Items may be of any type.
    """

# Two: select a random list item (with choice)
#   This challenge is mostly to demonstrate how great "choice()" is.
#   Do the same as for challenge one, but this time, you may use
#   the choice() function.


def random_item_with_choice(some_list: list):
    """Return a random item from the list

    :param some_list: a list of items. Items may be of any type
    """


# Three: random strings
#   In this challenge, you will use the choices() function to return
#   a random string from a provided character list.


def random_16_char_string_from_chars(chars: Union[str, Sequence]) -> str:
    """Return a random string of ``chars``, of length 16

    Given a string or an iterable sequence (e.g. a List or a Tuple)
    of characters, return a random assortment of those characters
    as a new string.

    Use the choices() method to accomplish this. You will probably
    also need some method to join up list items into a string!

    :param chars: the characters from which to choose.
    """


#
#
#
# # # Test Code # # #
#
#
#

# You shouldn't need to directly adjust anything in here, but you're
# encouraged to review and understand it.


@pytest.mark.parametrize('test_list', [
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    [1, 2, 3, 'boo', 'bop'],
])
def test_get_random_list_item_with_randint(test_list):
    """Test that a random list item is returned"""
    _assert_output_random(random_item_with_randint, test_list)
    source = getsource(random_item_with_randint)
    assert 'randint(' in source
    assert 'choice(' not in source


@pytest.mark.parametrize('test_list', [
    [1, 2, 3, 4, 5],
    ['a', 'b', 'c', 'd', 'e', 'f'],
    [1, 2, 3, 'boo', 'bop'],
])
def test_get_random_list_item_with_choice(test_list):
    """Test that a random list item is returned"""
    _assert_output_random(random_item_with_choice, test_list)
    source = getsource(random_item_with_choice)
    assert 'randint(' not in source
    assert 'choice(' in source


@pytest.mark.parametrize('test_chars', [
    'abc',
])
def test_random_16_char_string_from_chars(test_chars):
    """Test the random string generator"""


def _assert_output_random(func, arg):
    """Assert the output of a function is relatively random"""
    # call the function a number of times to get a variety of returns
    returns = [func(arg) for _ in range(50)]
    # converting to a set removes duplicate items
    set_ret = set(returns)
    # if the set is of a length other than one, it means we got *at least*
    # two different results, which is probably good enough
    assert len(set_ret) != 1, "All returns the same. That doesn't seem random"
    # now we check the source code to make sure the choice() function was
    # not used, and that randint was.


if __name__ == '__main__':
    args = ['-vx', __file__]  # base arguments

    if len(argv) == 2:
        # We got a particular function name to test, so we use pytest's
        # -k argument to find a test called test_<function_name>.
        # Note the use of a Python 3.6+ ONLY f-string
        # (see # https://www.python.org/dev/peps/pep-0498/)
        args.extend(['-k', f'test_{argv[1]}'])

    pytest.main(args)
