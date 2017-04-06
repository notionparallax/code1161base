# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""
from __future__ import division
from __future__ import print_function


def add_5(a_number):
    """Return a number that is 5 bigger than number given.

    This isn't a trick!
    First thing to do is to remove the pass. That's just tellign python that
    the empty block is intentional - it's python's "this page is intentionally
    left blank"
    Then you need to:
        return a_number plus five
    except expressed in python, not english
    """
    pass


def adder(a_number, another_number):
    """Add two numbers.

    Same as above, but with any two numbers.
    """
    pass


def shout(a_string):
    """Return a string in uppercase.

    look up the docs for string methods. Either in the official docs, here:
        https://docs.python.org/2/library/string.html
    or in any of the million places that google will give you.
    "python make a string uppercase" is a good starting search query.
    """
    pass


def really_shout(a_string):
    """Return a string in uppercase, with an exclamation mark on the end.

    In the spirit of being DRY (don't repeat yourself) reuse the shout function
    from above.
    Look up how to 'concatinate' strings to make this happen.
    """
    pass


def minitest(f, args, expected):
    """Run a function with a list of args and print a response.

    This is a helper. Don't edit it.
    """
    result = f(*args)
    template = "expect {name}({args}) == {expected} => {result}"
    print(template.format(name=f.__name__,
                          args=str(args)[1:-1],
                          result=result == expected,
                          expected=expected))
    return result == expected


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    minitest(add_5, [1], 6)
    minitest(add_5, [6], 11)
    minitest(add_5, [-3], 2)
    minitest(add_5, [0.5], 5.5)
    minitest(adder, [-0.5, -0.5], 1)
    minitest(adder, [2, 2], 4)
    minitest(adder, [2, -2], 0)
    minitest(shout, ["hello"], "HELLO")
    minitest(really_shout, ["hello"], "HELLO!")
    minitest(really_shout, [""], "!")
    minitest(really_shout, ["!"], "!!")
