"""
This Python challenge will help you to familiarize yourself with
Python's various modules for handling dates and times, including:

* time: https://docs.python.org/3/library/time.html
* datetime: https://docs.python.org/3/library/datetime.html

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
import time

from datetime import date, datetime, timedelta
from sys import argv
from typing import Union

import pytest


#
#
#
# # # Coding Challenges Begin # # #
#
#
#


# One: generating a Unix timestamp
#   Using either the datetime or the time module, write a function that
#   outputs the current number of seconds since the epoch (January 01,
#   1970), also known as a timestamp or a Unix/Linux timestamp.


def get_timestamp() -> int:
    """Return the current time as an integer timestamp

    .. hint::
        You may use either the time or the datetime module
        to accomplish this task
    """
    return int(time.time())

# Two: convert a datetime object into a Unix timestamp
#   Given a datetime object, return the corresponding Unix timestamp

def timestamp_from_datetime(dt: datetime) -> int:
    """Return the timestamp corresponding to the given datetime"""

    return int(dt.timestamp())

# Three: dates to strings
#   Given a date or datetime object, output a string representing
#   the date in the form "YYYY-mm-dd"

def date_to_string(date_or_datetime: Union[date, datetime]) -> str:
    """Return an ISO Date string (YYYY-mm-dd) for the given date

    .. hint::
        Because you have two object types here "date" and "datetime",
        the easiest thing to do would be to use a method that
        both objects types have available.

    :param date_or_datetime: a date or datetime object to convert
    """

    date_string = date_or_datetime.isoformat()

    return date_string[:10]

# Four: strings to dates
#   Given a date string in ISO format ("YYYY-mm-dd"), convert to a
#   date object and return

def string_to_date(date_string: str) -> date:
    """Return a date object corresponding to the passed string"""

    date_input = datetime.strptime(date_string, "%Y-%m-%d")
    return date_input.date()

# Five: comparisons to now
#   Given a datetime object, return True if it is in the future, False
#   if it is now or in the past

def is_future(dt: datetime) -> bool:
    """Return whether the passed datetime is in the future"""

    if dt > datetime.now():
        return True
    else:
        return False

# Six: adding time
#   Given a number of days, return a datetime object corresponding to
#   that number of days in the future

def days_from_today(days: int) -> date:
    """Return a date object for ``days`` from now

    .. hint::
        For this, you should use the ``timedelta`` objects.
        You will also need to get a date object corresponding
        to ``today``. There is probably a method for that...

    Ideally, this function should not balk at negative days.

    :param days: the number of days from now to return
    """
    return date.today() + timedelta(days=days)

#
#
#
# # # Test Code # # #
#
#
#

# You shouldn't need to directly adjust anything in here, but you're
# encouraged to review and understand it.


def test_get_timestamp():
    """Test the get_timestamp function"""
    ts = get_timestamp()
    assert isinstance(ts, int)
    assert isinstance(datetime.fromtimestamp(ts), datetime)


@pytest.mark.parametrize('dt', [
    datetime(2017, 5, 27),
    datetime(1970, 2, 3),
    datetime(4271, 12, 1),
    datetime(2016, 1, 12, 19, 27, 16),
    datetime(2016, 1, 12, 19, 27),
    datetime(2016, 1, 12, 19),
])
def test_timestamp_from_datetime(dt):
    """Test the timestamp_from_datetime function

    :param dt: the datetime object with which to test the function
    """
    ts = timestamp_from_datetime(dt)
    assert isinstance(ts, int)
    back_converted = datetime.fromtimestamp(ts)
    assert back_converted == dt


@pytest.mark.parametrize('dt, exp', [
    (datetime(2017, 12, 24, 12, 27, 1), '2017-12-24'),
    (datetime(2012, 5, 27), '2012-05-27'),
    (date(1999, 9, 12), '1999-09-12'),
    (date(3037, 1, 1), '3037-01-01'),
])
def test_date_to_string(dt, exp):
    """Test the date_to_string function

    :param dt: the date/datetime to input
    :param exp: the expected output
    """
    assert date_to_string(dt) == exp


@pytest.mark.parametrize('ds, exp', [
    ('2012-03-24', date(2012, 3, 24)),
    ('1988-12-19', date(1988, 12, 19)),
    ('3333-03-30', date(3333, 3, 30)),
    ('2017-11-01', date(2017, 11, 1)),
])
def test_string_to_date(ds, exp):
    """Test the string_to_date function

    :param ds: the date string to parse
    :param exp: the expected output
    """
    assert string_to_date(ds) == exp


@pytest.mark.parametrize('dt, exp', [
    (datetime.now(), False),
    (datetime.now() - timedelta(days=1), False),
    (datetime.now() + timedelta(days=1), True),
    (datetime.now() - timedelta(weeks=500), False),
    (datetime.now() + timedelta(weeks=10000), True),
])
def test_is_future(dt, exp):
    """Test the is_future function

    :param dt: the datetime object to input
    :param exp: the expected return
    """
    assert is_future(dt) is exp


@pytest.mark.parametrize('days', [
    12,
    24,
    3000,
    999999,
    -27,
    -1000,
])
def test_days_from_today(days):
    """Test the days_from_today function

    :param days: the number of days to input
    """
    exp = date.today() + timedelta(days=days)
    assert days_from_today(days) == exp


if __name__ == '__main__':
    args = ['-x', __file__]  # base arguments

    if len(argv) == 2:
        # We got a particular function name to test, so we use pytest's
        # -k argument to find a test called test_<function_name>.
        # Note the use of a Python 3.6+ ONLY f-string
        # (see # https://www.python.org/dev/peps/pep-0498/)
        args.extend(['-k', f'test_{argv[1]}'])

    pytest.main(args)
