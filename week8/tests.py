# -*- coding: UTF-8 -*-
"""Run the tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""
from __future__ import division
from __future__ import print_function
import imp
import os
import sys
import string
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import completion_message
from codeHelpers import ex_runs
from codeHelpers import nyan_cat
# from codeHelpers import syntax_error_message
from codeHelpers import test
from codeHelpers import test_flake8
from codeHelpers import Timeout

WEEK_NUMBER = 8


def theTests(path_to_code_to_check="."):
    """Run all the tests."""
    print("\nWelcome to the exam!")
    print("May the odds be ever in your favour.\nEspecially today!")

    testResults = []

    ex1path = "{}/week{}/exercise1.py".format(path_to_code_to_check,
                                              WEEK_NUMBER)

    if ex_runs(path_to_code_to_check, exNumber=1, weekNumber=WEEK_NUMBER):
        exam = imp.load_source("exercise1", ex1path)

        testResults.append(
            test(test_flake8(ex1path),
                 "Pass the linter"))

        testResults.append(
            test(exam.greet("the Queen") == "Hello the Queen",
                 "greet the Queen"))
        testResults.append(
            test(exam.greet("Pr♂nc♀♂") == "Hello Pr♂nc♀♂",
                 "greet Pr♂nc♀♂"))

        testResults.append(
            test(exam.three_counter([3, 3, 3, 3, 1]) == 4,
                 "three_counter [3, 3, 3, 3, 1]"))
        testResults.append(
            test(exam.three_counter([0, 1, 2, 5, -9]) == 0,
                 "three_counter [0, 1, 2, 5, -9]"))

        fizza = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11,
                 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz',
                 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29,
                 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38,
                 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47,
                 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56,
                 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz',
                 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74,
                 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83,
                 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92,
                 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
        testResults.append(
            test(exam.fizz_buzz() == fizza,
                 "fizz_buzz"))

        a = exam.put_behind_bars("a serial killer")
        testResults.append(
            test(a == "|a| |s|e|r|i|a|l| |k|i|l|l|e|r|",
                 "put_behind_bars"))
        a = exam.put_behind_bars("a bartender")
        testResults.append(
            test(a == "|a| |b|a|r|t|e|n|d|e|r|",
                 "put_behind_bars"))

        testResults.append(
            test(exam.pet_filter("x") == ['red fox'],
                 "pet_filter"))
        testResults.append(
            test(exam.pet_filter("q") == [],
                 "pet_filter"))
        testResults.append(
            test(exam.pet_filter("p") == ['pig', 'sheep', 'guinea pig', 'pigeon', 'alpaca', 'guppy'],
                 "pet_filter"))

        testResults.append(
            test(exam.best_letter_for_pets() == "e",
                 "best_letter_for_pets"))

        testResults.append(
            test(len(str(exam.make_filler_text_dictionary())) == 175,
                 "make_filler_text_dictionary"))

        filler1 = exam.random_filler_text(50)
        testResults.append(
            test(len(filler1.split(" ")) == 50 and len(filler1) > 3*50,
                 "random_filler_text"))

        filler2 = exam.fast_filler(1000)
        testResults.append(
            test(len(filler2.split(" ")) == 1000 and len(filler2) > 3*1000,
                 "first fast_filler"))

        testResults.append(
            test(exam.fast_filler(10)[0] in string.uppercase and
                 exam.fast_filler(10)[1] in string.lowercase,
                 "first fast_filler has a starting capital"))

        testResults.append(
            test(exam.fast_filler(10)[-1] == ".",
                 "first fast_filler ends with a ."))
        try:
            with Timeout(1):
                for _ in range(10):
                    exam.fast_filler(1000)
                testResults.append(
                    test(True,
                         "subsiquent fast_filler"))
        except Exception as e:
            print(e)
            testResults.append(
                test(False,
                     "subsiquent fast_filler wasn't fast enough"))

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
