"""
I'm in UR exam.

This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.

You've got an hour.
"""
from __future__ import division
from __future__ import print_function
import time


def greet(name="Towering Timmy"):
    """Return a greeting.

    return a string of "Hello" and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    return "Hello " + str(name)
    pass


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.

    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    counter = 0
    for item in input_list:
        if item == 3:
            counter += 1
    return counter
    pass


def fizz_buzz():
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!

       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
            from https://blog.codinghorror.com/why-cant-programmers-program/

    Return a list that has an integer if the number isn't special, and a string
    if it is. E.g. [1, 2, "Fizz", 4, "Buzz", 6, 7, ...]
    """
    fizzBuzzList = []
    # your code here
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("Fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("Buzz")
        else:
            fizzBuzzList.append(i)
    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.

    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: make sure that you have a pipe on both ends of the string.
    """
    broken = list(input_string)
    barred = [x+"|" for x in broken]
    return "|" + "".join(barred)
    pass


def pet_filter(letter="a"):
    """Return a list of animals with `letter` in their name."""
    pets = ["dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken",
            "guinea pig", "donkey", "duck", "water buffalo",
            "western honey bee", "dromedary camel", "horse", "silkmoth",
            "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca",
            "guineafowl", "ferret", "muscovy duck", "barbary dove",
            "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi",
            "canary", "society finch", "fancy mouse", "siamese fighting fish",
            "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"]
    in_list = []
    for p in pets:
        if letter in p:
            in_list.append(p)
    return in_list
    pass


def best_letter_for_pets():
    """Return the letter that is present in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string
    the_alphabet = string.lowercase
    best_letter = ""
    best_number = 0
    for letter in the_alphabet:
        count = len(pet_filter(letter))
        if count > best_number:
            best_number = count
            best_letter = letter
    return best_letter
    pass


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.

    There is a random word generator here: http://www.setgetgo.com/randomword/
    The only argument that the generator takes is the length of the word.

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g. {3: ['cat','pop','cow'], ...}
    Use the API to get the 3 words.
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. ?len=
    TIP: you'll need the requests library
    """
    import requests
    word_dictionary = {}
    for number in range(3, 8):
        word_dictionary[number] = []
        for word in range(3):
            url = "http://setgetgo.com/randomword/get.php?len=" + str(number)
            new_word = requests.get(url).text
            print(new_word)
            word_dictionary[number].append(new_word)
    return word_dictionary
    pass


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.

    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    TIP: you'll need the random library
    Bonus: extra mark if you get the paragraph to start with a
           capital letter and end with a full stop.
    """
    import random
    d = make_filler_text_dictionary()
    paragraph_list = []
    for _ in range(number_of_words):
        w = d[random.randint(3, 7)][random.randint(0, 2)]
        paragraph_list.append(w)
    return " ".join(paragraph_list)
    pass


def fast_filler(number_of_words=200):
    """Reimplement random filler text.

    This time, the first time the code runs, save the dictionary to a file.
    On the second run,if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.words"
    TIP: you'll need the os library
    TIP: you'll probably want to use json dumps and loads to get the dictionary
    into and out of the file. Be careful when you read it back in, it'll
    convert integer keys to strings.
    """
    import os
    import random
    import json

    if os.path.isfile("dict_racey.words"):
        f = open("dict_racey.words", 'r')
        d = json.loads(f.read())
        f.close()
    else:
        d = make_filler_text_dictionary()
        f = open("dict_racey.words", 'w')
        f.write(json.dumps(d))
        f.close()

    paragraph_list = []
    for _ in range(number_of_words):
        number_of_letters = str(random.randint(3, 7))
        which_word = random.randint(0, 2)
        w = d[number_of_letters][which_word]
        paragraph_list.append(w)
    return " ".join(paragraph_list)
    pass


if __name__ == '__main__':
    print(greet())
    print(three_counter())
    print(fizz_buzz())
    print(put_behind_bars())
    print(put_behind_bars("a serial killer"))
    print(put_behind_bars("a bartender"))
    print(pet_filter())
    print(pet_filter("p"))
    print(best_letter_for_pets())
    print(len(str(make_filler_text_dictionary())))
    print(random_filler_text())
    print(fast_filler())
    for i in range(10):
        print(i, fast_filler())
