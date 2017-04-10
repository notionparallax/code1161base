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
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import completion_message
from codeHelpers import nyan_cat
from codeHelpers import test
from codeHelpers import test_flake8
from codeHelpers import ex_runs

WEEK_NUMBER = 2


def ex2runs(path):
    """Test w2 ex2 to check it works."""
    try:
        if path:
            imp.load_source("exercise2",
                            os.path.join(path, "week"+str(WEEK_NUMBER)))
            return True
        else:
            import exercise2
            return True
        return exercise2.week2exersise2() == "MC Hammer"
    except Exception as e:
        print("\nThere is a syntax error", str(e))
        return False


def syntax_error_message(e):
    """Print a well formed error message."""
    print("something went wring with the import.\nProbably a syntax error.")
    print("does this file run properly on its own?\n" + str(e))
    return False


def ex3runs(path):
    """Test w2 ex3 to check it works."""
    try:
        # this annoys the linter, but I think the scoping is ok
        if path:
            imp.load_source("exercise3",
                            os.path.join(path, "week"+str(WEEK_NUMBER)))
            return True
        else:
            import exercise3
            return True
    except Exception as e:
        print("\nThere is a syntax error in exercise3", str(e))
        print('\n{s:{c}^{n}}\n{s:{c}^{n}}'.format(n=50, c='*', s=""))
        print("WARNING: there are more tests, but they won't run")
        print("until you fix the syntax errors in exercise3.py")
        print('{s:{c}^{n}}\n{s:{c}^{n}}\n'.format(n=50, c='*', s=""))
        return False


def theTests(path_to_code_to_check="."):
    """Run the tests."""
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("May the odds be ever in your favour.\n")

    testResults = []

    # Tests from here:
    path = "{}/week{}/exercise0.py".format(path_to_code_to_check, WEEK_NUMBER)
    testResults.append(
        test(test_flake8(path),
             "Exercise 0: pass the linter"))

    if ex_runs(path_to_code_to_check, exNumber=0, weekNumber=WEEK_NUMBER):
        exercise0 = imp.load_source("exercise0", path)

        testResults.append(
            test(exercise0.add_5(55) == 60,
                 "Exercise 0: add_5 - 55 + 5 = 60?"))
        testResults.append(
            test(exercise0.add_5(-5) == 0,
                 "Exercise 0: add_5 - -5 + 5 = 0?"))
        testResults.append(
            test(exercise0.add_5(0.1) == 5.1,
                 "Exercise 0: add_5 - 0.1 + 5 = 5.1?"))

        testResults.append(
            test(exercise0.adder(5, 5) == 10,
                 "Exercise 0: adder - 5 + 5 = 10?"))
        testResults.append(
            test(exercise0.adder(-5, -5) == -10,
                 "Exercise 0: adder - -5 + -5 = -10?"))
        testResults.append(
            test(exercise0.adder(0.1, 0.9) == 1,
                 "Exercise 0: adder - 0.1 + 0.9 = 1?"))

        testResults.append(
            test(exercise0.shout("you've") == "YOU'VE",
                 "Exercise 0: shout - you've => YOU'VE?"))
        testResults.append(
            test(exercise0.shout("got") == "GOT",
                 "Exercise 0: shout - got => GOT?"))
        testResults.append(
            test(exercise0.shout("to") == "TO",
                 "Exercise 0: shout - to => TO?"))

        testResults.append(
            test(exercise0.really_shout("fight") == "FIGHT!",
                 "Exercise 0: really_shout - fight => FIGHT!?"))
        testResults.append(
            test(exercise0.shout("for") == "FOR",
                 "Exercise 0: shout - for => FOR?"))
        testResults.append(
            test(exercise0.shout("your") == "YOUR",
                 "Exercise 0: shout - your => YOUR?"))
        testResults.append(
            test(exercise0.really_shout("right") == "RIGHT!",
                 "Exercise 0: really_shout - right => RIGHT!?"))
        testResults.append(
            test(exercise0.shout("to") == "TO",
                 "Exercise 0: shout - to => TO?"))
        testResults.append(
            test(exercise0.really_shout("PARTY") == "PARTY!",
                 "Exercise 0: really_shout - PARTY => PARTY!?"))

    path = "{}/week{}/exercise1.py".format(path_to_code_to_check, WEEK_NUMBER)
    testResults.append(
        test(test_flake8(path),
             "Exercise 1: pass the linter"))

    path = "{}/week{}/exercise2.py".format(path_to_code_to_check, WEEK_NUMBER)
    testResults.append(
        test(test_flake8(path),
             "Exercise 2: pass the linter"))

    testResults.append(
        test(ex2runs(path_to_code_to_check),
             "Exercise 2: debug the file"))

    path = "{}/week{}/exercise3.py".format(path_to_code_to_check, WEEK_NUMBER)
    testResults.append(
        test(test_flake8(path),
             "Exercise 3: pass the linter"))

    if ex3runs(path_to_code_to_check):
        exercise3 = imp.load_source("exercise3", path)
        # is odd
        testResults.append(
            test(exercise3.is_odd(2) is False,
                 "Exercise 3: is_odd - is 2 odd?"))

        testResults.append(
            test(exercise3.is_odd(5),
                 "Exercise 3: is_odd - is 5 odd?"))

        # fix it
        testResults.append(
            test(exercise3.fix_it(True, True) == "No Problem",
                 "Exercise 3: fix_it - it moves, and it should"))

        testResults.append(
            test(exercise3.fix_it(False, True) == "WD-40",
                 "Exercise 3: fix_it - it doesn't move, and it should"))

        testResults.append(
            test(exercise3.fix_it(True, False) == "Duct Tape",
                 "Exercise 3: fix_it - it moves, and it shouldn't"))

        testResults.append(
            test(exercise3.fix_it(False, False) == "No Problem",
                 "Exercise 3: fix_it - it doesn't move, and it shouldn't"))

        # loops
        tenStars = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
        testResults.append(
            test(exercise3.loops_1a() == tenStars,
                 "Exercise 3: loops_1a - 1d for loop"))

        bang_star = ["!", "*", "!", "*", "!", "*", "!", "*", "!", "*"]
        testResults.append(
            test('map' in exercise3.star_map.func_code.co_names and
                 exercise3.star_map() == bang_star,
                 "Exercise 3: loops_1b - 1d map"))

        testResults.append(
            test(exercise3.loops_1c(3, ":)") == [':)', ':)', ':)'],
                 "Exercise 3: loops_1c - 1d with arguments"))

        ten_by_ten_stars = [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ]
        testResults.append(
            test(exercise3.loops_2() == ten_by_ten_stars,
                 "Exercise 3: loops_2 - 10×10 stars"))

        ten_matching_numbers = [
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
            ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
            ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
            ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
            ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
            ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
            ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
            ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
        ]
        testResults.append(
            test(exercise3.loops_3() == ten_matching_numbers,
                 "Exercise 3: loops_3 - 10 matching lists"))

        ten_rising_lists = [
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ]
        testResults.append(
            test(exercise3.loops_4() == ten_rising_lists,
                 "Exercise 3: loops_4 - ten rising lists"))

        coords = [
            ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)'],
            ['(i1, j0)', '(i1, j1)', '(i1, j2)', '(i1, j3)', '(i1, j4)'],
            ['(i2, j0)', '(i2, j1)', '(i2, j2)', '(i2, j3)', '(i2, j4)'],
            ['(i3, j0)', '(i3, j1)', '(i3, j2)', '(i3, j3)', '(i3, j4)'],
            ['(i4, j0)', '(i4, j1)', '(i4, j2)', '(i4, j3)', '(i4, j4)'],
            ['(i5, j0)', '(i5, j1)', '(i5, j2)', '(i5, j3)', '(i5, j4)'],
            ['(i6, j0)', '(i6, j1)', '(i6, j2)', '(i6, j3)', '(i6, j4)'],
            ['(i7, j0)', '(i7, j1)', '(i7, j2)', '(i7, j3)', '(i7, j4)'],
            ['(i8, j0)', '(i8, j1)', '(i8, j2)', '(i8, j3)', '(i8, j4)'],
            ['(i9, j0)', '(i9, j1)', '(i9, j2)', '(i9, j3)', '(i9, j4)']
        ]
        testResults.append(
            test(exercise3.loops_5() == coords,
                 "Exercise 3: loops_5 - write the coords"))

        wedge = [
            ['0'],
            ['0', '1'],
            ['0', '1', '2'],
            ['0', '1', '2', '3'],
            ['0', '1', '2', '3', '4'],
            ['0', '1', '2', '3', '4', '5'],
            ['0', '1', '2', '3', '4', '5', '6'],
            ['0', '1', '2', '3', '4', '5', '6', '7'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
            ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ]
        testResults.append(
            test(exercise3.loops_6() == wedge,
                 "Exercise 3: loops_6 - make a wedge"))

        pyramid = [
            [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
            [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
            [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*']
        ]
        testResults.append(
            test(exercise3.loops_7() == pyramid,
                 "Exercise 3: loops_7 - pyramid of stars"))

    print("{0}/{1} (passed/attempted)".format(sum(testResults),
                                              len(testResults)))

    if sum(testResults) == len(testResults):
        print(nyan_cat())
        message = "Rad, you've got all the tests passing!"
        completion_message(message, len(message) + 2)

    return {"of_total": len(testResults),
            "mark": sum(testResults),
            "results": testResults}


if __name__ == "__main__":
    theTests()  # no arg, runs tests on local code
