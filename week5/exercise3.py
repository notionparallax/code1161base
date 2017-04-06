"""Recursion.

Exercises and examples to illustrate recursion.
"""
from __future__ import division
from __future__ import print_function
import turtle


def koch(t, order, size):
    """Make turtle t draw a Koch fractal of 'order' and 'size'.

    Leave the turtle facing the same direction.
    """
    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)


def draw_koch():
    """Open a tk window and show the turtle drawing the koch curve.

    Docs for python turtles here.
    https://docs.python.org/2/library/turtle.html
    """
    raphael = turtle.Turtle()
    raphael.speed(1000)
    raphael.penup()
    raphael.goto(-180, 0)
    raphael.pendown()
    koch(raphael, 5, 360)


def square_koch():
    r"""Draw a koch curve with a square rather than a triancular point.

           _
    e.g. _| |_ rather than _/\_
    """
    #  TODO: Ben, work out how to mark this.
    #  Save a screen grab? Can the turtle library do this?
    pass


def abba(source="abba", guard=5):
    """Recursively replace letters acording to the rules.

    This function takes a seed string, e.g. "abba" and replaces each letter in
    turn acording to the rules. These rules can be of arbitrary complexity.

    Modify the rules to map from "abba" to baobab
    TODO: check that this is possible.
    """
    def apply_rules(letter):
        if letter == "a":
            return "bba"
        elif letter == "b":
            return "ab"
        else:
            print("something is dramatically wrong")

    print(source)
    source = list(source)  # convert "abba" to ["a", "b", "b", "a"]
    result = map(apply_rules, source)
    new_string = "".join(result)
    guard -= 1
    if guard > 0:
        abba(new_string, guard)
    else:
        return new_string


abba()


def itallian_dinner(axiom="tomatoes", guard=10):
    """Make recursive dinner plans.

    # The Italian dinner
    In Douglas Hofstader's _Metamagical Themas_ (a compendium of essays he
    wrote for _Scientific American_ when he took over from martin Gardiner),
    there is a typically funny, but useful, introduction to production systems
    based on a recursive replacement algorithm to generate Italian recipes.
    Production systems are examples of recursive algorithms, that is, they are.
    TODO search for this text online
    """
    pass


if __name__ == '__main__':
    draw_koch()
