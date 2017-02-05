# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import mock
import sys
import os
sys.path.append(os.path.dirname(__file__)[:-5])
from codeHelpers import test, test_flake8, completion_message

WEEK_NUMBER = 3


def syntax_error_message(e):
    print "something went wring with the import.\nProbably a syntax error."
    print "does this file run properly on its own?\n" + str(e)
    return False


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
    try:
        import exercise1
    except Exception as e:
        return syntax_error_message(e)

    mockInputs = ["aword", [1, 2, 3], {"an": "object"}] + range(low - 25, high + 20, 5)
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
        import exercise3
    except Exception as e:
        return syntax_error_message(e)

    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise3.advancedGuessingGame() == "You got it!"
    except Exception as e:
        print "exception:", e


def ex1runs():
    try:
        # this annoys the linter, but I think the scoping is ok
        import exercise1
        return True
    except Exception as e:
        print "\nThere is a syntax error in exercise1", str(e)
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

test_super_asker

testResults.append(
    test(test_flake8("week{}/exercise2.py".format(WEEK_NUMBER)),
         "Exercise 2: pass the linter"))

testResults.append(
    test(test_example_guessingGame(),
         "Exercise 2: example guessing game"))

upperBound = 15
lowerBound = 10
guesses = range(lowerBound, upperBound + 1)
mockInputs = [lowerBound] + [upperBound] + guesses
testResults.append(
    test(test_advanced_guessingGame(mockInputs),
         "Exercise 4: guessing game, U&L"))

mockInputs = ["ten"] + [lowerBound] + [upperBound] + ["cats"] + guesses
testResults.append(
    test(test_advanced_guessingGame(mockInputs),
         "Exercise 4: guessing game, polite failures"))

print "{0}/{1} (passed/attempted)".format(sum(testResults), len(testResults))

if sum(testResults) == len(testResults):
    print nyan_cat()
    message = "Cowabunga! You've got all the tests passing!"
    completion_message(message, len(message) + 2)
