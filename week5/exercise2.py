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
"""

from __future__ import division
from __future__ import print_function

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


def countdown(message, start, stop, completion_message):
    pass


""" This should be a function called tell_me_about_this_right_triangle
    it should return a dictionary of triangle facts, keys should include: Area,
    perimeter, height, base, hypotinuse aspect (could be tall or wide)
    It should optionally print information as a nicely formatted string. Make
    printing turned off by default but turned on with an optional argument."""
triangle = {"base": 3, "height": 4}
triangle["hypotenuse"] = triangle["base"]**2 + triangle["height"]**2
print("area = " + str((triangle["base"] * triangle["height"])/2))
print("side lengths are:")
print("base: " + triangle["base"])
print("height: " + triangle["height"])
print("hypotinuse: " + triangle["hypotinuse"])

another_hyp = 5**2 + 6**2
print(another_hyp)

yet_another_hyp = 40**2 + 30**2
print(yet_another_hyp)


def calculate_hypotinuse(base, height):
    return hypotinuse


def get_triangle_facts(base, height, units="mm"):
    return {"area": None,
            "perimeter": None,
            "height": None,
            "base": None,
            "hypotinuse": None,
            "aspect": None}


def tell_me_about_this_right_triangle(facts_dictionary):
    return """
    This triangle is {area}{units}²
    It has a perimeter of {}{units}
    {height}
    |
    |     |\\
    |____>| \\  {hypotinuse}
          |  \\
          |   \\
          ------
          {base}

    This is a {aspect} triangle.
    """


def print_triangle_things():
    facts_dictionary = get_triangle_facts(base, height, units="mm")
    print(tell_me_about_this_right_triangle(facts_dictionary))


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


wordy_pyramid()


def get_a_word_of_length_n():
    """."""
    pass


def list_of_words_with_lengths(list_of_lengths):
    """."""
    pass
