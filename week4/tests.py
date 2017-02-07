# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""


import sys
import os
import exercise1
sys.path.append(os.path.dirname(__file__)[:-5])
from codeHelpers import test, test_flake8, completion_message

WEEK_NUMBER = 4


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

testDict = {'lastName': u'hoogmoed',
            'password': u'jokers',
            'postcodePlusID': 4311240}
testResults.append(
    test(exercise1.get_some_details() == testDict,
         "Exercise 1: get some data out of a JSON file"))

lengths = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 18, 16, 14, 12, 10, 8, 6, 4]
testResults.append(
    test([len(w) for w in exercise1.wordy_pyramid()] == lengths,
         "Exercise 1: request some simple data from the internet"))

# testResults.append(
#     test(ex1runs(),
#          "Exercise 1: EXPLAIN TEST HERE"))

print "{0}/{1} (passed/attempted)".format(sum(testResults), len(testResults))

if sum(testResults) == len(testResults):
    message = "Rad, you've got all the tests passing!"
    completion_message(message, len(message) + 2)
