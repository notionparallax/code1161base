# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

import mock
import sys
import os
sys.path.append(os.path.dirname(__file__)[:-5])
from codeHelpers import test, test_flake8


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


def test_example_guessingGame():
    try:
        import exercise3
    except Exception as e:
        return syntax_error_message(e)
    upperBound = 5
    guesses = range(5+1)
    mockInputs = [upperBound] + guesses
    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise3.exampleGuessingGame() == "You got it!"
    except Exception as e:
        print "exception:", e


def test_advanced_guessingGame(mockInputs):
    try:
        import exercise4
    except Exception as e:
        return syntax_error_message(e)

    try:
        with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
            return exercise4.advancedGuessingGame() == "You got it!"
    except Exception as e:
        print "exception:", e


print "\nWelcome to week 2! May the odds be ever in your favour.\n"

testResults = []
testResults.append(
    test(test_flake8('week2/exercise1.py'),
         "Exercise 1: pass the linter"))

testResults.append(
    test(test_flake8('week2/exercise2.py'),
         "Exercise 2: pass the linter"))

testResults.append(
    test(ex2runs(),
         "Exercise 2: debug the file"))

testResults.append(
    test(test_flake8('week2/exercise3.py'),
         "Exercise 3: pass the linter"))

testResults.append(
    test(test_example_guessingGame(),
         "Exercise 3: example guessing game"))

testResults.append(
    test(test_flake8('week2/exercise4.py'),
         "Exercise 4: pass the linter"))

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
