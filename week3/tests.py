# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import math
import mock
import os
import sys
sys.path.append(os.path.dirname(__file__)[:-5])
from codeHelpers import test, test_flake8, completion_message, nyan_cat

WEEK_NUMBER = 3


def syntax_error_message(exNumber, e):
    print "There is a syntax error in exercise{}\n{}".format(exNumber, str(e))
    print '\n{s:{c}^{n}}\n{s:{c}^{n}}'.format(n=50, c='*', s="")
    print "WARNING: there are more tests, but they won't run"
    print "until you fix the syntax errors in exercise{}.py".format(exNumber)
    print '{s:{c}^{n}}\n{s:{c}^{n}}\n'.format(n=50, c='*', s="")


def test_stubborn_asker(low, high):
    try:
        import exercise1
    except Exception as e:
        return syntax_error_message(e)

    mockInputs = range(low - 25, high + 20, 5)
    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return low <= exercise1.stubborn_asker(low, high) <= high
    except Exception as e:
        print "exception:", e


def test_not_number_rejector():
    try:
        import exercise1
    except Exception as e:
        return syntax_error_message(e)

    mockInputs = ["aword", [1, 2, 3], {"an": "object"}, 40]
    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise1.not_number_rejector()
    except Exception as e:
        print "exception:", e


def test_super_asker(low, high):
    dirty_things = ["aword", [1, 2, 3], {"an": "object"}]
    neat_range = range(low - 25, high + 20, 5)
    mockInputs = dirty_things + neat_range
    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise1.super_asker(low, high)
    except Exception as e:
        print "exception:", e


def test_example_guessingGame():
    try:
        import exercise2
    except Exception as e:
        return syntax_error_message(e)
    upperBound = 5
    guesses = range(5+1)
    mockInputs = [upperBound] + guesses
    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise2.exampleGuessingGame() == "You got it!"
    except Exception as e:
        print "exception:", e


def test_advanced_guessingGame(mockInputs):
    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise3.advancedGuessingGame() == "You got it!"
    except Exception as e:
        print "exception:", e


def test_binary_search(low, high, actual):
    BASE2 = 2
    b = exercise4.binary_search(low, high, actual)
    if b is not None:
        return b < math.log(high - low, BASE2)
    else:
        return False


def ex1runs():
    try:
        # this annoys the linter, but I think the scoping is ok
        import exercise1
        return True
    except Exception as e:
        syntax_error_message(1, e)
        return False


def ex3runs():
    try:
        # this annoys the linter, but I think the scoping is ok
        import exercise3
        return True
    except Exception as e:
        syntax_error_message(3, e)
        return False


def ex4runs():
    try:
        # this annoys the linter, but I think the scoping is ok
        import exercise4
        return True
    except Exception as e:
        syntax_error_message(4, e)
        return False


print "\nWelcome to week {}!".format(WEEK_NUMBER)
print "May the odds be ever in your favour.\n"

testResults = []

testResults.append(
    test(test_flake8("week{}/exercise1.py".format(WEEK_NUMBER)),
         "Exercise 1: pass the linter"))

if ex1runs():
    import exercise1
    testResults.append(
        test(exercise1.loop_ranger(3, 8, 1) == [3, 4, 5, 6, 7],
             "Exercise 1: Loop ranger (3, 8, 1)"))
    testResults.append(
        test(exercise1.loop_ranger(100, 104, 2) == [100, 102],
             "Exercise 1: Loop ranger (100, 104, 2)"))

    testResults.append(
        test(exercise1.lone_ranger(3, 8, 1) == [3, 4, 5, 6, 7],
             "Exercise 1: Lone ranger (3, 8, 1)"))
    testResults.append(
        test(exercise1.lone_ranger(100, 104, 2) == [100, 102],
             "Exercise 1: Lone ranger (100, 104, 2)"))

    testResults.append(
        test(exercise1.two_step_ranger(100, 104) == [100, 102],
             "Exercise 1: Two step ranger (100, 104)"))
    testResults.append(
        test(exercise1.two_step_ranger(0, 10) == [0, 2, 4, 6, 8],
             "Exercise 1: Two step ranger (100, 104)"))

    testResults.append(
        test(exercise1.gene_krupa_range(0, 10, 2, 1) == [0, 2, 3, 5, 6, 8, 9],
             "Exercise 1: gene_krupa_range (0, 10, 2, 1)"))
    testResults.append(
        test(exercise1.gene_krupa_range(0, 100, 30, 7) == [0, 30, 37, 67, 74],
             "Exercise 1: gene_krupa_range (0, 10, 2, 1)"))

    testResults.append(
        test(test_stubborn_asker(50, 60),
             "Exercise 1: Stubborn asker"))
    testResults.append(
        test(test_stubborn_asker(10, 20),
             "Exercise 1: Stubborn asker"))

    testResults.append(
        test(test_not_number_rejector(),
             "Exercise 1: not_number_rejector"))

    testResults.append(
        test(test_super_asker(50, 60),
             "Exercise 1: test_super_asker"))

testResults.append(
    test(test_flake8("week{}/exercise2.py".format(WEEK_NUMBER)),
         "Exercise 2: pass the linter"))

testResults.append(
    test(test_example_guessingGame(),
         "Exercise 2: example guessing game"))

if ex3runs():
    import exercise3

    testResults.append(
        test(test_flake8("week{}/exercise3.py".format(WEEK_NUMBER)),
             "Exercise 3: pass the linter"))

    upperBound = 15
    lowerBound = 10
    guesses = range(lowerBound, upperBound + 1)
    mockInputs = [lowerBound] + [upperBound] + guesses
    testResults.append(
        test(test_advanced_guessingGame(mockInputs),
             "Exercise 3: guessing game, U&L"))

    mockInputs = ["ten"] + [lowerBound] + [upperBound] + ["cats"] + guesses
    testResults.append(
        test(test_advanced_guessingGame(mockInputs),
             "Exercise 3: guessing game, polite failures"))

if ex4runs():
    import exercise4

    testResults.append(
        test(test_flake8("week{}/exercise4.py".format(WEEK_NUMBER)),
             "Exercise 4: pass the linter"))

    testResults.append(
        test(test_binary_search(1, 100, 5),
             "Exercise 4: binary_search(1, 100, 5)"))
    testResults.append(
        test(test_binary_search(1, 100, 95),
             "Exercise 4: binary_search(1, 100, 95)"))
    testResults.append(
        test(test_binary_search(1, 51, 5),
             "Exercise 4: binary_search(1, 51, 5)"))
    testResults.append(
        test(test_binary_search(1, 50, 5),
             "Exercise 4: binary_search(1, 50, 5)"))

print "{0}/{1} (passed/attempted)".format(sum(testResults), len(testResults))

if sum(testResults) == len(testResults):
    print nyan_cat()
    message = "Cowabunga! You've got all the tests passing!"
    completion_message(message, len(message) + 2)
