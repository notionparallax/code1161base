# -*- coding: UTF-8 -*-
"""Run the tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""
from __future__ import division
from __future__ import print_function
import imp
import math
import mock
import os
import random
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import completion_message
from codeHelpers import ex_runs
from codeHelpers import nyan_cat
from codeHelpers import syntax_error_message
from codeHelpers import test
from codeHelpers import test_flake8
from codeHelpers import Timeout

WEEK_NUMBER = 3


def test_stubborn_asker(path, low, high):
    """Test the stubborn asker function."""
    try:
        path = "{}/week{}/exercise1.py".format(path, WEEK_NUMBER)
        exercise1 = imp.load_source("exercise1", path)
    except Exception as e:
        return syntax_error_message(4, e)

    mockInputs = range(low - 25, high + 20, 5)
    try:
        with Timeout(3):
            with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
                return low <= exercise1.stubborn_asker(low, high) <= high
    except Exception as e:
        print("exception:", e)


def test_not_number_rejector(path):
    """Test the not number rejector function."""
    try:
        path = "{}/week{}/exercise1.py".format(path, WEEK_NUMBER)
        exercise1 = imp.load_source("exercise1", path)
    except Exception as e:
        return syntax_error_message(1, e)

    mockInputs = ["aword", [1, 2, 3], {"an": "object"}, 40]
    try:
        with Timeout(3):
            with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
                return exercise1.not_number_rejector("Testing some values:")
    except Exception as e:
        print("exception:", e)


def test_super_asker(path, low, high):
    """Test the super asker function."""
    try:
        path = "{}/week{}/exercise1.py".format(path, WEEK_NUMBER)
        exercise1 = imp.load_source("exercise1", path)
    except Exception as e:
        return syntax_error_message(1, e)

    dirty_things = ["aword", [1, 2, 3], {"an": "object"}]
    neat_range = range(low - 25, high + 20, 5)
    mockInputs = dirty_things + neat_range
    try:
        with Timeout(3):
            with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
                return exercise1.super_asker(low, high)
    except Exception as e:
        print("exception:", e)


def test_example_guessingGame(path):
    """Test the example_guessingGame function.

    This should always pass becasue it's provided code
    """
    try:
        path = "{}/week{}/exercise2.py".format(path, WEEK_NUMBER)
        exercise2 = imp.load_source("exercise2", path)
    except Exception as e:
        return syntax_error_message(2, e)
    upperBound = 5
    guesses = range(5+1)
    mockInputs = [upperBound] + guesses
    try:
        with Timeout(3):
            with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
                return exercise2.exampleGuessingGame() == "You got it!"
    except Exception as e:
        print("exception:", e)


def test_advanced_guessingGame(path, mockInputs):
    """Test the advanced_guessingGame function."""
    try:
        path = "{}/week{}/exercise3.py".format(path, WEEK_NUMBER)
        exercise3 = imp.load_source("exercise3", path)
    except Exception as e:
        return syntax_error_message(3, e)

    try:
        with Timeout(3):
            with mock.patch('__builtin__.raw_input', side_effect=mockInputs):
                return exercise3.advancedGuessingGame() == "You got it!"
    except Exception as e:
        print("exception:", e)


def test_binary_search(path, low, high, actual):
    """Test the binary search function.

    checks to see that it's searching better than O(log n)
    """
    try:
        path = "{}/week{}/exercise4.py".format(path, WEEK_NUMBER)
        exercise4 = imp.load_source("exercise4", path)
        BASE2 = 2
        b = None
        with Timeout(3):
            b = exercise4.binary_search(low, high, actual)
            b["WorstCaseO"] = math.log(high - low, BASE2)
            print("b", b)
        if b is not None:
            print("snuck it in")
            return b["tries"] < b["WorstCaseO"]
        else:
            return False
    except Exception as e:
        return syntax_error_message(4, e)


def vis_binary_search_performance(path="."):
    """Provide a visualisation of the performance of the binary search."""
    try:
        path = "{}/week{}/exercise4.py".format(path, WEEK_NUMBER)
        exercise4 = imp.load_source("exercise4", path)
    except Exception as e:
        return syntax_error_message(4, e)

    import matplotlib.pyplot as plt
    BASE2 = 2
    results = []
    testRuns = 1000
    for _ in range(testRuns):
        low = random.randint(-100, 100)
        high = random.randint(low + 2, 200)
        guess = random.randint(low + 1, high - 1)
        bs = exercise4.binary_search(low, high, guess)
        # print bs, low, high, guess
        tries = bs['tries']
        worst = math.log(high - low, BASE2)
        ratio = tries/worst
        results.append(ratio)
    plt.hist(results)
    plt.title("Proportion of worst case performance "
              "over {} iterations".format(testRuns))
    print("""
This histogram shows the number of guesses that it took the search to
find the answer. The big O worst case is the base 2 log of the range that
you're guessing within. In other words, what power of two fills that space?
E.g. if your range is 16, then the worst case is 4 guesses: 2×2×2×2 = 16
Think back to when you were playing the game with your brain, sometimes
you'd go over the worst case because you aren't a perfect arithmatic
machine but the computer is, so it's always below that worst case limit.

            Close the histogram to finish running the tests.""")
    plt.show()


def theTests(path_to_code_to_check="."):
    """Run all the tests."""
    print("\nWelcome to week {}!".format(path_to_code_to_check, WEEK_NUMBER))
    print("May the odds be ever in your favour.\n")

    testResults = []

    # Give each person 10 seconds to complete all tests.
    ex1path = "{}/week{}/exercise1.py".format(path_to_code_to_check,
                                              WEEK_NUMBER)
    testResults.append(
        test(test_flake8(ex1path), "Exercise 1: pass the linter"))

    if ex_runs(path_to_code_to_check, exNumber=1, weekNumber=WEEK_NUMBER):
        exercise1 = imp.load_source("exercise1", ex1path)

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
            test(exercise1.gene_krupa_range(0, 10, 2, 1) ==
                 [0, 2, 3, 5, 6, 8, 9],
                 "Exercise 1: gene_krupa_range(0, 10, 2, 1)"))
        testResults.append(
            test(exercise1.gene_krupa_range(0, 100, 30, 7) ==
                 [0, 30, 37, 67, 74],
                 "Exercise 1: gene_krupa_range(0, 100, 30, 7)"))

        testResults.append(
            test(test_stubborn_asker(path_to_code_to_check, 50, 60),
                 "Exercise 1: Stubborn asker"))

        testResults.append(
            test(test_stubborn_asker(path_to_code_to_check, 10, 20),
                 "Exercise 1: Stubborn asker"))

        testResults.append(
            test(test_not_number_rejector(path_to_code_to_check),
                 "Exercise 1: not_number_rejector"))

        testResults.append(
            test(test_super_asker(path_to_code_to_check, 50, 60),
                 "Exercise 1: test_super_asker"))

    local_path = "{}/week{}/exercise2.py".format(path_to_code_to_check,
                                                 WEEK_NUMBER)
    testResults.append(
        test(test_flake8(local_path),
             "Exercise 2: pass the linter"))

    testResults.append(
        test(test_example_guessingGame(path_to_code_to_check),
             "Exercise 2: example guessing game"))

    if ex_runs(path_to_code_to_check, exNumber=3, weekNumber=WEEK_NUMBER):
        imp.load_source("exercise3",
                        os.path.join(path_to_code_to_check,
                                     "week"+str(WEEK_NUMBER)))

        to_lint = "{}/week{}/exercise3.py".format(path_to_code_to_check,
                                                  WEEK_NUMBER)
        testResults.append(
            test(test_flake8(to_lint),
                 "Exercise 3: pass the linter"))

        lowerBound = 10
        upperBound = 15
        guesses = range(lowerBound, upperBound + 1)
        mockInputs = [lowerBound] + [upperBound] + guesses
        testResults.append(
            test(test_advanced_guessingGame(path_to_code_to_check,
                                            mockInputs),
                 "Exercise 3: guessing game, U&L"))

        mockInputs = ["ten"] + [lowerBound] + [upperBound] + \
                     ["cats"] + guesses
        testResults.append(
            test(test_advanced_guessingGame(path_to_code_to_check,
                                            mockInputs),
                 "Exercise 3: guessing game, polite failures"))

        lowerBound = 15
        upperBound = 10
        secondGuess = 25
        guesses = range(lowerBound, secondGuess + 1)
        mockInputs = [lowerBound] + [upperBound] + [secondGuess] + guesses
        testResults.append(
            test(test_advanced_guessingGame(path_to_code_to_check,
                                            mockInputs),
                 "Exercise 3: guessing game, lowerBound "
                 "bigger than upperBound"))

        lowerBound = 10
        upperBound = 11
        secondGuess = 15
        guesses = range(lowerBound, secondGuess + 1)
        mockInputs = [lowerBound] + [upperBound] + [secondGuess] + guesses
        testResults.append(
            test(test_advanced_guessingGame(path_to_code_to_check,
                                            mockInputs),
                 "Exercise 3: guessing game, no " +
                 "range to guess in (delta 1)"))

        lowerBound = 10
        upperBound = 10
        secondGuess = 15
        guesses = range(lowerBound, secondGuess + 1)
        mockInputs = [lowerBound] + [upperBound] + [secondGuess] + guesses
        testResults.append(
            test(test_advanced_guessingGame(path_to_code_to_check,
                                            mockInputs),
                 "Exercise 3: guessing game, no " +
                 "range to guess in (equal)"))

    if ex_runs(path_to_code_to_check, exNumber=4, weekNumber=WEEK_NUMBER):
        path = "{}/week{}/exercise4.py".format(path_to_code_to_check,
                                               WEEK_NUMBER)
        imp.load_source("exercise4", path)

        testResults.append(
            test(test_flake8(path),
                 "Exercise 4: pass the linter"))

        try_these = [(1, 100, 5),
                     (1, 100, 6),
                     (1, 100, 95),
                     (1, 51, 5),
                     (1, 50, 5)]
        for i in range(10):
            try_these.append((0, 100, random.randint(1, 99)))

        for tv in try_these:
            print(tv)
            try:
                testResults.append(  # *tv unpacks this tuple ------v
                    test(test_binary_search(path_to_code_to_check, *tv),
                         "Exercise 4: binary_search" +
                         "({}, {}, {})".format(*tv)))
            except Exception:
                print("********\n\nfailed:", tv)
                print("tv failure", Exception)
                # raise ValueError("********\n\nfailed: {}".format(tv))
                testResults.append(0)

        # if the binary search is working, show a graph of guess numbers
        if test(test_binary_search(path_to_code_to_check, 1, 10, 5), ""):
            # If you aren't Ben, then show the histogram
            if "ben/projects/git" not in os.path.dirname(__file__):
                vis_binary_search_performance()

    print("{0}/{1} (passed/attempted)".format(sum(testResults),
                                              len(testResults)))

    if sum(testResults) == len(testResults):
        print(nyan_cat())
        message = "Cowabunga! You've got all the tests passing!"
        completion_message(message, len(message) + 2)

    return {"of_total": len(testResults),
            "mark": sum(testResults),
            "results": testResults}


if __name__ == "__main__":
    theTests()
