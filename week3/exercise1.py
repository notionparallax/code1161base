# -*- coding: UTF-8 -*-
"""
Modify each function until the tests pass
"""


def loop_ranger(start, stop=None, step=1):
    """
    return a list of numbers between start and stop in steps of step
    Do this using any method apart from just using range()
    """
    return [i for i in range(start, stop, step)]
    pass


def lone_ranger(start, stop, step):
    """
    loop_ranger duplicate the functionality of range.
    Look up the docs for range() and wrap it in a 1:1 way
    """
    return range(start, stop, step)
    pass


def two_step_ranger(start, stop):
    """
    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    return range(start, stop, 2)
    pass


def gene_krupa_range(start, stop, even_step, odd_step):
    """
    make a list that instead of having evenly spaced steps
    make odd steps be one size and even steps be another.
    """
    latest = start
    the_list = []
    index = 0
    while latest < stop:
        the_list.append(latest)
        if index % 2 == 0:
            latest = latest + even_step
        else:
            latest = latest + odd_step
        index += 1
    return the_list
    pass


def stubborn_asker(low, high):
    """
    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "Give me a number between {low} and {high}:".format(low=low,
                                                                  high=high)
    while True:
        input_number = int(raw_input(message))
        if low <= input_number <= high:
            print "Thanks, {} looks good!".format(input_number)
            return input_number
        else:
            print "{} isn't between {} and {}!".format(input_number, low, high)


def not_number_rejector():
    """
    Ask for a number, and if the response isactually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    """
    message = "Give me a number: "
    while True:
        user_input = raw_input(message)
        try:
            int(user_input)  # try it to trigger failure
            print "Thanks, {} looks good!".format(user_input)
            return int(user_input)
        except:
            print "{} isn't a number! try again:".format(user_input)


def super_asker(low, high):
    """
    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "Give me a number between {low} and {high}:".format(low=low,
                                                                  high=high)
    while True:
        user_input = ""
        input_number = ""
        user_input = raw_input(message)
        try:
            input_number = int(user_input)
            if low <= input_number <= high:
                print "Thanks, {} looks good!".format(input_number)
                return input_number
            else:
                print "{} isn't between {} and {}!".format(input_number,
                                                           low,
                                                           high)
        except:
            print "{} isn't a number! try again:".format(user_input)


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print "\nloop_ranger", loop_ranger(1, 10, 2)
    print "\nlone_ranger", lone_ranger(1, 10, 3)
    print "\ntwo_step_ranger", two_step_ranger(1, 10)
    print "\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5)
    print "\nstubborn_asker"
    stubborn_asker(30, 45)
    print "\nnot_number_rejector"
    not_number_rejector()
    print "\nsuper_asker"
    super_asker(33, 42)
