"""
Modify each function until the tests pass
"""


def is_odd(a_number):
    """
    return True if a_number is odd,
    and False if a_number is even.
    Look into modulo division using the '%' operator as one way of doing this.
    """
    pass


def fix_it(moves=True, should_move=True):
    """
    Using the engineerign flowchart for the rules, return the apropriate
    response to the input parameters.
    Use conditional statements: if, else, elif etc.
    """
    pass


def loops_1a():
    """
    using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    stars = []
    for i in range(10):
        stars.append('*')
    return stars


def loops_1b():
    """
    using a map
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    pass


def loops_1c(number_of_items=5, symbol="#"):
    """
    using any method
    return a list of number_of_items items, each one
    a string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']
    """
    pass


def loops_2():
    """
    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
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
    """
    stars = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append('*')
        stars.append(row)
    return stars


def loops_3():
    """

    """
    pass


def loops_4():
    """

    """
    pass


def loops_5():
    """

    """
    pass


def loops_6():
    """

    """
    pass


def loops_7():
    """

    """
    pass


def loops_8():
    """

    """
    pass


def loops_9():
    """
     err
    """
    pass


def lp(some_kind_of_list, exercise_name):
    """
    This is a helper function that prints your
    results to check that they are tidy.
    """
    if some_kind_of_list is not None:
        print "\n" + exercise_name
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print column,
                print
        else:
            for column in some_kind_of_list:
                print column,
            print
    else:
        print exercise_name, "maybe you haven't got to this one yet?"


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    lp(is_odd(1), "is_odd")
    lp(is_odd(4), "is_odd")
    lp(fix_it(), "fix_it")
    lp(loops_1a(), "loops_1a")
    lp(loops_1b(), "loops_1b")
    lp(loops_1c(), "loops_1c")
    lp(loops_2(), "loops_2")
    lp(loops_3(), "loops_3")
    lp(loops_4(), "loops_4")
    lp(loops_5(), "loops_5")
    lp(loops_6(), "loops_6")
    lp(loops_7(), "loops_7")
    lp(loops_8(), "loops_8")
    lp(loops_9(), "loops_9")
