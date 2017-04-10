# -*- coding: UTF-8 -*-
"""Recursion.

Exercises and examples to illustrate recursion.
"""
from __future__ import division
from __future__ import print_function
import turtle


def abba(source="abba", guard=5):
    """Recursively replace letters acording to the rules.

    This function takes a seed string, e.g. "abba" and replaces each letter in
    turn acording to the rules. These rules can be of arbitrary complexity.

    Modify the rules to map from:

                   abba
                    to
               bbaaobaobbba
                    to
    aobaobbbabbaoaaobbbaoaaobaobaobbba
                and so on...
    """
    def apply_rules(letter):
        if letter == "a":
            return "bba"
        elif letter == "b":
            return "aob"
        elif letter == "o":
            return "oa"
        else:
            return letter

    print(source)
    source = list(source)  # convert "abba" to ["a", "b", "b", "a"]
    result = map(apply_rules, source)
    new_string = "".join(result)
    guard -= 1
    if guard > 0:
        abba(new_string, guard)
    else:
        return new_string


def italian_dinner(axiom="tomatoes", guard=10):
    """Make recursive dinner plans.

    # The Italian dinner

    In Douglas Hofstader's _Metamagical Themas_ (a compendium of essays he
    wrote for _Scientific American_ when he took over from martin Gardiner),
    there is a typically funny, but useful, introduction to production systems
    based on a recursive replacement algorithm to generate Italian recipes.
    Production systems are examples of recursive algorithms, that is, they are
    functions that use as input the output of their own results on earlier
    operations.

    The most general way of characterising a production system is to see it as
    a formal language based on symbol manipulation. They habe much in common
    with formal systems in logic in that:
        1.  they start with an axiom, which is given of the formal system;
        2.  there are a set of statements inthe formal system which can be
            thought of as theroums of the system; and
        3.  there are a set of rules for transforming any statement which is
            part of the formal system into any other using replacement rules.
    In the itallian dinner, teh axiom is of course _tomatoes_

    Note that in order for this to work, we need to habe at least one word in
    the right-hand side that matches one of the words in the left-hand side.
    If we do not do this then the production system will not catch, and it will
    fail to expand into the florid ingredients list.

    From Paul Coates, Programming.Architecture
    I would strongly recomend reading this book!

    referencing: DOUGLAS R. HOFSTADTER, Metamagical Themas
    https://archive.org/stream/MetamagicalThemas/Metamagical%20Themas,%20Hofstadter_djvu.txt
    """
    # TODO: get the real table for this!
    def rules(word):
        if word == "tomatoes":
            return "delicious tomatoes with linguini"
        elif word == "linguini":
            return "linguini and basil"
        elif word == "basil":
            return "pesto made from basil and tomatoes"
        elif word == "delicious":
            return "delicious and runny pesto"
        else:
            return word

    print(axiom)
    axiom = axiom.split(" ")  # convert "abba" to ["a", "b", "b", "a"]
    result = map(rules, axiom)
    new_string = " ".join(result)
    guard -= 1
    if guard > 0:
        italian_dinner(new_string, guard)
    else:
        return new_string
    pass


def koch(t, order, size):
    """Make turtle t draw a Koch fractal of 'order' and 'size'."""
    trace = ""
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        trace += koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        trace += koch(t, order-1, size/3)
        t.right(120)
        trace += koch(t, order-1, size/3)
        t.left(60)
        trace += koch(t, order-1, size/3)
    return str(order) + trace


def draw_koch(drawing_method, steps_deep=4):
    """Open a tk window and show the turtle drawing the koch curve.

    Docs for python turtles here.
    https://docs.python.org/2/library/turtle.html
    """
    raphael = turtle.Turtle()
    raphael.speed(1000)
    raphael.penup()
    raphael.goto(-300, 0)
    raphael.pendown()
    trace = drawing_method(raphael, order=steps_deep, size=600)
    return trace


def square_koch(t, order, size):
    r"""Draw a koch curve with a square rather than a triangular point.

           _
    e.g. _| |_ rather than _/\_

    Leave the turtle facing the same direction.

    """
    trace = ""
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        trace += square_koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(90)
        trace += square_koch(t, order-1, size/3)
        t.right(90)
        trace += square_koch(t, order-1, size/3)
        t.right(90)
        trace += square_koch(t, order-1, size/3)
        t.left(90)
        trace += square_koch(t, order-1, size/3)
    return str(order) + trace
    pass


if __name__ == '__main__':
    print(draw_koch(drawing_method=square_koch, steps_deep=4))
    print(draw_koch(drawing_method=koch, steps_deep=4))
    abba()
    # italian_dinner()
