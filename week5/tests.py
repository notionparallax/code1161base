# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""


import sys
import os
sys.path.append(os.path.dirname(__file__)[:-5])
from codeHelpers import test, test_flake8, completion_message

WEEK_NUMBER = 5


def ex1runs():
    try:
        import exercise1
        return exercise1.function_that_returns_something()
    except Exception as e:
        print "\nThere is a syntax error", str(e)
        return False


def syntax_error_message(e):
    print "something went wring with the import.\nProbably a syntax error."
    print "does this file run properly on its own?\n" + str(e)
    return False


print "\nWelcome to week {}!".format(WEEK_NUMBER)
print "May the odds be ever in your favour.\n"

testResults = []

# stack the test here #
testResults.append(
    test(test_flake8("week{}/exercise1.py".format(WEEK_NUMBER)),
         "Exercise 1: pass the linter"))

testResults.append(
    test(ex1runs(),
         "Exercise 1: EXPLAIN TEST HERE"))


print "{0}/{1} (passed/attempted)".format(sum(testResults), len(testResults))

if sum(testResults) == len(testResults):
    message = "Rad, you've got all the tests passing!"
    completion_message(message, len(message) + 2)
