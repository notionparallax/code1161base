# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import inspect
import os
import re
import sys
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


def strip_docstring(a_function):
    regex = r"\"\"\"[\s\w\.\'\"\&\!\#\%]*\"\"\""
    theFunction = inspect.getsource(a_function)
    return re.sub(regex, "", theFunction)


def syntax_error_message(e):
    print "something went wring with the import.\nProbably a syntax error."
    print "does this file run properly on its own?\n" + str(e)
    return False


def ex3runs():
    try:
        # this annoys the linter, but I think the scoping is ok
        import exercise3
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
             "Exercise 3: is_odd - is 2 odd?"))

    testResults.append(
        test(exercise3.is_odd(5),
             "Exercise 3: is_odd - is 5 odd?"))

    testResults.append(
        test(exercise3.fix_it(True, True),
             "Exercise 3: fix_it - it moves, and it should"))

    testResults.append(
        test(exercise3.fix_it(False, True),
             "Exercise 3: fix_it - it doesn't move, and it should"))

    testResults.append(
        test(exercise3.fix_it(True, False),
             "Exercise 3: fix_it - it moves, and it shouldn't"))

    testResults.append(
        test(exercise3.fix_it(False, False),
             "Exercise 3: fix_it - it doesn't move, and it shouldn't"))

    testResults.append(
        test(exercise3.loops_1(),
             "Exercise 3: loops_1 - "))

    testResults.append(
        test(exercise3.loops_2(),
             "Exercise 3: loops_2 - "))

    testResults.append(
        test(exercise3.loops_3(),
             "Exercise 3: loops_3 - "))

    testResults.append(
        test(exercise3.loops_4(),
             "Exercise 3: loops_4 - "))

    testResults.append(
        test(exercise3.loops_5(),
             "Exercise 3: loops_5 - "))

    testResults.append(
        test(exercise3.loops_6(),
             "Exercise 3: loops_6 - "))

    testResults.append(
        test(exercise3.loops_7(),
             "Exercise 3: loops_7 - "))

    testResults.append(
        test(exercise3.loops_8(),
             "Exercise 3: loops_8 - "))

    testResults.append(
        test(exercise3.loops_9(),
             "Exercise 3: loops_9 - "))





print 'map' in strip_docstring(exercise3.loops_9)

print "{0}/{1} (passed/attempted)".format(sum(testResults), len(testResults))
