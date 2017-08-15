"""
This Python challenge will help to refresh your knowledge of
string parsing methods. It will also introduce you to
URL-parsing methods and regular expressions.

String documentation:
* https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

urllib.parse documentation:
* https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse

Regular expressions:
* https://docs.python.org/3/library/re.html

Introduction to regular expressions:
* http://www.aivosto.com/vbtips/regex.html

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
from sys import argv
from typing import Tuple

import pytest


#
#
#
# # # Coding Challenges Begin # # #
#
#
#


# One: parsing a URL into parts with string methods
#   Write a function that converts a URL into a tuple of the form:
#   (protocol, host, port, path, query_string). If an item is not
#   present in the URL, it should be an empty string in the resultant 
#   tuple. All items in the returned tuple should be strings. The path 
#   should include the leading slash (e.g. /index, not index), by 
#   convention. The query string should not include the leading question 
#   mark. If the path is just a slash (e.g. www.google.com/ instead of
#   www.google.com), the slash should be retained, and the path returned
#   as '/'.
#
#   Example URLs and expected returns:
#   - http://www.google.com
#       ('http', 'www.google.com', '', '', '')
#   - https://localhost:8080/api
#       ('https', 'localhost', '8080', '/api', '')
#   - http://192.168.12.2/index?login=true
#       ('http', '192.168.12.2', '', '/index', 'login=true')
#   - https://www.twitter.com:9090/api/posts/27?expand=1
#       ('https', 'www.twitter.com', '9090', '/api/posts/27', 'expand=1')


def url_tuple(url: str) -> Tuple[str, str, str, str, str]:
    """Split a URL into a 5-tuple of strings

    The 5-tuple should be of the form::

        (protocol, host, port, path, query_string)

    """

    final_list = []

    if url:
        protocol_split = url.split('://')
        protocol = protocol_split[0]
        working_url = protocol_split[1]
    else:
        return '', '', '', '', ''

    if '?' in url:
        query_split = working_url.split('?')
        query = query_split[1]
        working_url = query_split[0]
    else:
        query = ''

    if '/' in working_url:
        path_split = working_url.split('/')
        path = '/' + path_split[1]
        contains_host = path_split[0]
    else:
        path = ''
        contains_host = working_url

    if ':' in contains_host:
        port_split = contains_host.split(':')
        host = port_split[0]
        port = port_split[1]
    else:
        host = contains_host
        port = ''

    final_list.extend([protocol, host, port, path, query])
    return tuple(final_list)


def url_tuple_regex(url: str) -> Tuple[str, str, str, str, str]:
    """Split a URL into five parts

    https://regexone.com

    The parts should be the same as the method above, and the
    output should be the same as for the method above, but
    this time, use a regular expression to parse the URL.

    Hints:

    * Make regular reference to https://docs.python.org/3/library/re.html
    * You will only need one regular expression
    * Regular expression groups are created with parentheses
    * Regular expression groups can be marked as optional!
    * Regular expression groups can be referenced by number, but they
      can also be named and referenced by name
    * You can mark an entire regular expression group as occurring
      0 or any number of times (*), one or any number of times (+),
      or 0 or 1  time (?)
    * Parentheses denote groups. Square brackets denote character sets.
      Square brackets may be part of a parentheses-denoted group.
    * Square brackets are "greedy" by default, matching as many
      characters in the search string as match the character set.
    * You should consider installing the "regex tester" plugin for
      PyCharm. It's very helpful for developing regular expressions

    Tips:

    * This will almost certainly feel overwhelming at first. Regular
      expressions are extremely powerful, and like most things that
      are such, they are also rather complicated. But keep at it,
      use the regex tester, and you'll be fine!
    * You can probably find a StackOverflow question that will
      literally solve this challenge for you by giving you an
      appropriate regular expression. Try to avoid using that
      unless you have exhausted all your patience.
    * The difference between "find", "match", and "fullmatch" is that
      with "find", the regex just has to be anywhere in the
      string, with "match" it must match at the start of the string,
      and with "fullmatch", it must match the entirety of the string
    * Given that you don't just want to find a pattern in a string,
      but to match an entire string, you'll want to use "match" or
      "fullmatch"
    * A nice thing about the regex library in Python is that you can
      pre-compile your regular expressions, with
      ``re.compile(r'regex')`` (the "r" before the string means
      "raw", so no character escaping, like with slashes, is performed.
      A pre-compiled regex can be assigned to a variable and used
      a bunch of times with no performance overhead. As an example,
      consider the following two ways of solving the same problem,
      parsing a phone number to get its parts::

        import re

        string_one = '228-555-1234'
        string_two = '858-556-7890'

        # First approach, using re.compile()

        regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

        match_one = regex.match(string_one)
        match_two = regex.match(string_two)

        assert match_one is not None
        assert match_two is not None

        assert match_one.groups() == ('228', '555', '1234')
        assert match_two.groups() == ('858', '556', '7890')

        assert match_one.group(1) == '228'

        # Second approach, no pre-compilation

        match_one = regex.match(r'(\d{3})-(\d{3})-(\d{4})', string_one)
        match_two = regex.match(r'(\d{3})-(\d{3})-(\d{4})', string_two)

        assert match_one is not None
        assert match_two is not None

        assert match_one.groups() == ('228', '555', '1234')
        assert match_two.groups() == ('858', '556', '7890')

        assert match_one.group(1) == '228'

      * It should be clear that both approaches yield the same results,
        but the first, in addition to being less typing, only requires
        compiling the regular expression once, while the second requires
        compiling the expression in each call to ``match()``.

    """
    import re

    regex = re.compile(r'^(https?)://([^/:\?]+):?(\w*)(/?\w*)\??(\S*)')
    match = regex.match(url)

    return match.groups()


#
#
# Tests
#
#


TEST_URLS_AND_EXP_RESULTS = (
    ('https://www.google.com',
     ('https', 'www.google.com', '', '', '')),
    ('http://www.google.com:10',
     ('http', 'www.google.com', '10', '', '')),
    ('http://www.foo.org/in',
     ('http', 'www.foo.org', '', '/in', '')),
    ('http://www.foo.org/in?y=n',
     ('http', 'www.foo.org', '', '/in', 'y=n')),
    ('http://localhost:8080/',
     ('http', 'localhost', '8080', '/', '')),
    ('http://192.168.1.2:555/admin',
     ('http', '192.168.1.2', '555', '/admin', '')),
)


@pytest.mark.parametrize('url, exp', TEST_URLS_AND_EXP_RESULTS)
def test_url_tuple(url, exp):
    """Test the url_tuple function

    :param url: the url to test
    :param exp: the expected split url
    """
    assert url_tuple(url) == exp


@pytest.mark.parametrize('url, exp', TEST_URLS_AND_EXP_RESULTS)
def test_url_tuple_regex(url, exp):
    """Test the url_tuple_regex function

    :param url: the url to test
    :param exp: the expected split url
    """
    assert url_tuple_regex(url) == exp


if __name__ == '__main__':
    args = ['-x', __file__, '-s']  # base arguments

    if len(argv) == 2:
        # We got a particular function name to test, so we use pytest's
        # -k argument to find a test called test_<function_name>.
        # Note the use of a Python 3.6+ ONLY f-string
        # (see # https://www.python.org/dev/peps/pep-0498/)
        args.extend(['-k', f'test_{argv[1]}'])

    pytest.main(args)
