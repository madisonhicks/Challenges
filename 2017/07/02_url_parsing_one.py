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




@pytest.mark.parametrize('url, exp', [
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
])
def test_url_tuple(url, exp):
    """Test the url_tuple function

    :param url: the url to test
    :param exp: the expected split url
    """
    assert url_tuple(url) == exp


if __name__ == '__main__':
    args = ['-x', __file__, '-s']  # base arguments

    if len(argv) == 2:
        # We got a particular function name to test, so we use pytest's
        # -k argument to find a test called test_<function_name>.
        # Note the use of a Python 3.6+ ONLY f-string
        # (see # https://www.python.org/dev/peps/pep-0498/)
        args.extend(['-k', f'test_{argv[1]}'])

    pytest.main(args)
