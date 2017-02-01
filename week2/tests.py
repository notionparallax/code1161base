# -*- coding: UTF-8 -*-
"""
This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""
from colorama import Fore, Style
import inspect
import mock
import os


def test(testResult, name):
    if testResult:
        print(Fore.GREEN + "✔ " + name + Style.RESET_ALL)
    else:
        print(Fore.RED + "✘ " + name + Style.RESET_ALL)


def test_flake8(fileName):
    test_dir = os.path.dirname(os.path.abspath(inspect.getfile(
        inspect.currentframe())))

    files = [os.path.join(test_dir, fileName)]
    print files
    # Import the legacy API as flake8 3.0 currently has no official
    # public API - this has to be changed at some point.
    from flake8.api import legacy as flake8
    style_guide = flake8.get_style_guide()
    report = style_guide.check_files(files)

    if report.total_errors == 0:
        return True
    else:
        print report.total_errors
        return False


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

test(test_flake8('exercise1.py'), "Exercise 1: pass the linter")

test(test_flake8('exercise2.py'), "Exercise 2: pass the linter")

test(ex2runs(), "Exercise 2: debug the file")

test(test_example_guessingGame(), "Exercise 3: example guessing game")

upperBound = 15
lowerBound = 10
guesses = range(lowerBound, upperBound + 1)
mockInputs = [lowerBound] + [upperBound] + guesses
test(test_advanced_guessingGame(mockInputs), "Exercise 4: guessing game, U&L")

mockInputs = ["ten"] + [lowerBound] + [upperBound] + ["cats"] + guesses
test(test_advanced_guessingGame(mockInputs), "Exercise 4: guessing game, polite failures")
