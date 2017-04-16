# -*- coding: UTF-8 -*-
"""Test week 5's code.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

from __future__ import division
from __future__ import print_function
import imp
# import math
import os
# import requests
import sys
# import time
# from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import completion_message
from codeHelpers import nyan_cat
from codeHelpers import test
from codeHelpers import test_flake8
from codeHelpers import test_pydocstyle
from codeHelpers import grumpy


WEEK_NUMBER = 5
PASS = 1
FAIL = 0
LOCAL = os.path.dirname(os.path.realpath(__file__))


def test_diagrams(diagram, expected):
    """Test, crudely, that the correct diagram is being returned."""
    if expected == "tall" and "\\" in diagram:
        return True
    if expected == "wide" and "∕" in diagram:
        return True
    if expected == "equal" and "⋱" in diagram:
        return True
    print(grumpy())
    return False


def test_word_length(word, requested_length, expected_length):
    """Check that word lenths are as expected.

    Requesting a word less than 3 chars long should fail.
    """
    if type(requested_length) is str and word is not None:
        print("This API returns a random word if you malform the url\n",
              "You'll need to typecheck the input. I.e. check\n",
              "if type(length) is int:\n",
              "....#and so on\n",
              "It also does the same thing if you go under 3 characters\n",
              "long, so remember to check for that too!")
        print(grumpy())
    if expected_length is None and word is None:
        return True
    if len(word) == requested_length and len(word) == expected_length:
        return True
    print("Something a bit odd is happening")
    print("word:", word,
          "requested_length:", requested_length,
          "expected_length:", expected_length)
    print(grumpy())
    return False


def theTests(path_to_code_to_check="."):
    """Run the tests."""
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("May the odds be ever in your favour.\n")

    testResults = []

    # stack the tests below here
    path = "{}/week{}/exercise1.py".format(path_to_code_to_check, WEEK_NUMBER)
    print(path)

    e1 = imp.load_source("exercise1", path)

    # Linter test
    print("Linter test:", path)
    testResults.append(
        test(test_flake8(path),
             "Exercise 1: pass the linter"))

    # pydocstyle test
    print("Docstyle test:", path)
    testResults.append(
        test(test_pydocstyle(path),
             "Exercise 1: pass the pydocstyle test"))

    # countdown test
    book_of_counts = [{"message": "let's get ready to rumble",
                       "start": 8, "stop": 1,
                       "completion_message": "*rumbling sound*"},
                      {"message": "prepare to die in this many ways:",
                       "start": 0, "stop": 15,
                       "completion_message": "or not, I guess"}]
    for countdown in book_of_counts:
        try:
            the_countdown = e1.countdown(**countdown)
            if (len(the_countdown) > 0):
                [print(x) for x in the_countdown]
            else:
                print("Nothing to see here yet")
            expected = abs(countdown["start"] - countdown["stop"])+1
            testResults.append(
                test(len(the_countdown) == expected,
                     "Exercise 1: countdown!!"))
        except Exception as e:
            print("countdown test failed", e)
            testResults.append(FAIL)

    triangles = [{
                  'area': 6.0,
                  'aspect': 'tall',
                  'base': 3, 'height': 4,
                  'hypotenuse': 5.0,
                  'perimeter': 12.0,
                  'units': 'mm'},
                 {
                  'area': 15,
                  'aspect': 'wide',
                  'base': 10,
                  'height': 3,
                  'hypotenuse': 10.44030650891055,
                  'perimeter': 23.440306508910552,
                  'units': 'mm'},
                 {
                  'area': 60.0,
                  'aspect': 'tall',
                  'base': 8, 'height': 15,
                  'hypotenuse': 17.0,
                  'perimeter': 40.0,
                  'units': 'mm'},
                 {
                  'area': 12.5,
                  'aspect': 'equal',
                  'base': 5, 'height': 5,
                  'hypotenuse': 7.0710678118654755,
                  'perimeter': 17.071067811865476,
                  'units': 'mm'},
                 {
                  'area': 180.0,
                  'aspect': 'tall',
                  'base': 9, 'height': 40,
                  'hypotenuse': 41.0,
                  'perimeter': 90.0,
                  'units': 'mm'}]

    pattern = "Exercise {}: {}: {}×{}⇨{}"
    for t in triangles:
        hyp = e1.calculate_hypotenuse(t["base"], t["height"])
        testResults.append(
            test(hyp == t["hypotenuse"],
                 pattern.format(1,
                                "calculate_hypotenuse",
                                t["base"],
                                t["height"],
                                t["hypotenuse"])))

        area = e1.calculate_area(t["base"], t["height"])
        testResults.append(
            test(area == t["area"],
                 pattern.format(1,
                                "calculate_area",
                                t["base"],
                                t["height"],
                                t["area"])))

        aspect = e1.calculate_aspect(t["base"], t["height"])
        testResults.append(
            test(aspect == t["aspect"],
                 pattern.format(1,
                                "calculate_aspect",
                                t["base"],
                                t["height"],
                                t["aspect"])))

        perimeter = e1.calculate_perimeter(t["base"], t["height"])
        testResults.append(
            test(perimeter == t["perimeter"],
                 pattern.format(1,
                                "calculate_perimeter",
                                t["base"],
                                t["height"],
                                t["perimeter"])))

        facts = e1.get_triangle_facts(t["base"], t["height"])
        testResults.append(
            test(facts == t,
                 pattern.format(1,
                                "get_triangle_facts",
                                t["base"],
                                t["height"],
                                t)))

        facts = e1.get_triangle_facts(t["base"], t["height"])
        diagram = e1.tell_me_about_this_right_triangle(facts)
        testResults.append(
            test(test_diagrams(diagram=diagram,
                               expected=facts["aspect"]),
                 "exercise 1: draw a diagram\n" + diagram))

    ff = e1.triangle_master(base=5,
                            height=5,
                            return_diagram=False,
                            return_dictionary=False)
    tf = e1.triangle_master(base=5,
                            height=5,
                            return_diagram=True,
                            return_dictionary=False)
    ft = e1.triangle_master(base=5,
                            height=5,
                            return_diagram=False,
                            return_dictionary=True)
    tt = e1.triangle_master(base=5,
                            height=5,
                            return_diagram=True,
                            return_dictionary=True)
    testResults.append(
        test(ff is None,
             "exercise 1: triangle_master diagram: F, dictionary: F"))
    testResults.append(
        test(type(tf) is str,
             "exercise 1: triangle_master diagram: T, dictionary: F"))
    testResults.append(
        test(type(ft) is dict and
             "units" in ft["facts"] and
             type(ft["facts"]) is dict,
             "exercise 1: triangle_master diagram: F, dictionary: T"))
    testResults.append(
        test(type(tt) is dict and type(tt["diagram"]) is str,
             "exercise 1: triangle_master diagram: T, dictionary: T"))

    pattern = "Exercise 1: get_triangle_facts uses {}"
    for function_name in ["calculate_hypotenuse", "calculate_area",
                          "calculate_perimeter", "calculate_aspect"]:
        testResults.append(
            test(function_name in e1.get_triangle_facts.func_code.co_names,
                 pattern.format(function_name)))

    for length in zip([5, 8, 4, 0, "a"], [5, 8, 4, None, None]):
        word = e1.get_a_word_of_length_n(length[0])
        print(word, length)
        testResults.append(
            test(test_word_length(word=word,
                                  requested_length=length[0],
                                  expected_length=length[1]),
                 "exercise 1: get_a_word_of_length_n {}".format(word)))

    some_lengths = [[4, 5, 6], [4, 18, 4]]
    for lengths in some_lengths:
        words = e1.list_of_words_with_lengths(lengths)
        checks = [len(x[0]) == x[1] for x in zip(words, lengths)]
        print(words, lengths, checks)
        testResults.append(
            test(all(checks),
                 "exercise 1: list_of_words_with_lengths {}".format(word)))

    testResults.append(
        test("list_of_words_with_lengths" in
             e1.wordy_pyramid.func_code.co_names,
             "exercise 1: wordy_pyramid has been refactored"))

    lengths = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20,
               18, 16, 14, 12, 10, 8, 6, 4]
    works = None
    try:
        words = e1.wordy_pyramid()
        expected = [len(w) for w in words]
        works = expected == lengths
        print("expected     ", expected, "\ngiven lengths", lengths)
        [print(w + " " + str(len(w))) for w in words]
    except Exception as e:
        works = False
        print("Exercise 1: wordy_pyramid is broken", e)
    testResults.append(
        test(works, "Exercise 1: wordy_pyramid still works"))

    # EXERCISE 2 tests
    path = "{}/week{}/exercise2.py".format(path_to_code_to_check, WEEK_NUMBER)
    print(path)

    e2 = imp.load_source("exercise2", path)

    # Linter test
    print("Linter test:", path)
    testResults.append(
        test(test_flake8(path),
             "Exercise 2: pass the linter"))

    # pydocstyle test
    print("Docstyle test:", path)
    testResults.append(
        test(test_pydocstyle(path),
             "Exercise 2: pass the pydocstyle test"))

    source = ["baaab",
              "b",
              "roof",
              "hell"]
    result = ["bbaoaaobaobaobbbaaobaobbbaaobaobbbabbaoaaob",
              "bbaoaaob",
              "roabbaoabbaf",
              "hell"]
    for source, result in zip(source, result):
        testResults.append(
            test(e2.abba(source, 2) == result,
                 "exercise 2: abba {}⇨{}".format(source, result)))

    testResults.append(
        test(e2.draw_square(2) == "2100000100000100000100000100000",
             "exercise 2: Koch _|-|_"))
    testResults.append(
        test(e2.draw_pointy(2) == "210000100001000010000",
             "exercise 2: Koch _^_"))

    # CLEANUP AND FINISH

    print("{0}/{1} (passed/attempted)".format(sum(testResults),
                                              len(testResults)))

    if sum(testResults) == len(testResults):
        nyan_cat()
        message = "Rad, you've got all the tests passing!"
        completion_message(message, len(message) + 2)
        # treat()

    return {"of_total": len(testResults),
            "mark": sum(testResults),
            "results": testResults}


if __name__ == "__main__":
    theTests()
