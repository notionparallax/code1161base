# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should read as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.
"""

from __future__ import division
from __future__ import print_function
import math
import requests


def do_bunch_of_bad_things():
    """."""
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")


    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"]**2 + triangle["height"]**2
    print("area = " + str((triangle["base"] * triangle["height"])/2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5**2 + 6**2
    print(another_hyp)

    yet_another_hyp = 40**2 + 30**2
    print(yet_another_hyp)


def countdown(message, start, stop, completion_message):
    """."""
    if start > stop:
        step = -1
    elif start == stop:
        return "Huston, we have a problem"
    else:
        step = 1
    messages = []
    for i in range(start, stop, step):
        m = "{message} {i}".format(message=message, i=i)
        messages.append(m)
    messages.append(completion_message)

    return messages


# TRIANGLES
"""
This should be a series of functions that are ultimatly used by triangle_master
It should return a dictionary of triangle facts. It should optionally print
information as a nicely formatted string. Make printing turned off by default
but turned on with an optional argument.
"""


def calculate_hypotenuse(base, height):
    """."""
    return math.sqrt(base**2 + height**2)


def calculate_area(base, height):
    """."""
    return (base * height)/2


def calculate_perimeter(base, height):
    """."""
    return base + height + calculate_hypotenuse(base, height)


def calculate_aspect(base, height):
    """."""
    if base == height:
        return "equal"
    elif base > height:
        return "wide"
    elif base < height:
        return "tall"
    else:
        raise ValueError("your base and height are all munted")
    pass


def get_triangle_facts(base, height, units="mm"):
    """."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


def tell_me_about_this_right_triangle(facts_dictionary):
    """."""
    tall = """
{height}
|
|     |\\
|____>| \\  {hypotenuse}
      |  \\
      |   \\
      ------
      {base}"""
    wide = """
{hypotenuse}
 ↓         ∕ |
       ∕     | <-{height}
   ∕         |
∕------------|
  {base}"""
    equal = """
{height}
|
|     |⋱
|____>|  ⋱ <-{hypotenuse}
      |____⋱
      {base}"""

    pattern = """
This triangle is {area}{units}²
It has a perimeter of {perimeter}{units}
This is a {aspect} triangle."""

    facts = pattern.format(**facts_dictionary)
    if facts_dictionary["aspect"] == "tall":
        return tall.format(**facts_dictionary) + facts
    elif facts_dictionary["aspect"] == "equal":
        return equal.format(**facts_dictionary) + facts
    elif facts_dictionary["aspect"] == "wide":
        return wide.format(**facts_dictionary) + facts


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """."""
    if return_diagram and return_dictionary:
        return {"diagram": "diagram",
                "dictionary": "dictionary"}
    elif return_diagram:
        return "diagram"
    elif return_dictionary:
        return {"facts": "dictionary", "units": "yeah, right"}
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """."""
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL + str(i)
        r = requests.get(url)
        message = r.text
        pyramid_list.append(message)
    for i in range(0, 17, 2):
        url = baseURL + str(20 - i)
        r = requests.get(url)
        message = r.text
        pyramid_list.append(message)
    return pyramid_list

# def wordy_pyramid():
#     up = list_of_words_with_lengths(range(3, 21, 2))
#     dn = list_of_words_with_lengths(range(20, 3, -2))
#     [print(w) for w in up + dn]
#     return up + dn


def get_a_word_of_length_n(length):
    """."""
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    try:
        if length > 3 and type(length) is int:
            url = baseURL + str(length)
            r = requests.get(url)
            return r.text
        else:
            return None
    except:
        return None


def list_of_words_with_lengths(list_of_lengths):
    """."""
    return [get_a_word_of_length_n(i) for i in list_of_lengths]


def do_bunch_of_good_things():
    """."""
    wordy_pyramid()


if __name__ == "__main__":
    do_bunch_of_good_things
