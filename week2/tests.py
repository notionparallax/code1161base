# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import sys
import os
import inspect
sys.path.append(os.path.dirname(__file__)[:-5])
from codeHelpers import test, test_flake8

WEEK_NUMBER = 2


def ex2runs():
    try:
        import exercise2
        return exercise2.week2exersise2() == "MC Hammer"
    except Exception as e:
        print "\nThere is a syntax error", str(e)
        return False


def syntax_error_message(e):
    print "something went wring with the import.\nProbably a syntax error."
    print "does this file run properly on its own?\n" + str(e)
    return False


def ex3runs():
    try:
        import exercise3  # this annoys the linter, but I think the scoping is ok
        return True
    except Exception as e:
        print "\nThere is a syntax error in exercise3", str(e)
        print '\n{s:{c}^{n}}\n{s:{c}^{n}}'.format(n=50, c='*', s="")
        print "WARNING: there are more tests, but they won't run"
        print "until you fix the syntax errors in exercise3.py"
        print '{s:{c}^{n}}\n{s:{c}^{n}}\n'.format(n=50, c='*', s="")
        return False


print "\nWelcome to week {}!".format(WEEK_NUMBER)
print "May the odds be ever in your favour.\n"

testResults = []
testResults.append(
    test(test_flake8("week{}/exercise1.py".format(WEEK_NUMBER)),
         "Exercise 1: pass the linter"))

testResults.append(
    test(test_flake8("week{}/exercise2.py".format(WEEK_NUMBER)),
         "Exercise 2: pass the linter"))

testResults.append(
    test(ex2runs(),
         "Exercise 2: debug the file"))

testResults.append(
    test(test_flake8("week{}/exercise3.py".format(WEEK_NUMBER)),
         "Exercise 3: pass the linter"))

if ex3runs():
    import exercise3
    testResults.append(
        test(exercise3.is_odd(2) is False,
             "Exercise 3: is 2 odd?"))

    testResults.append(
        test(exercise3.is_odd(5),
             "Exercise 3: is 2 odd?"))

print "{0}/{1} (passed/attempted)".format(sum(testResults), len(testResults))
