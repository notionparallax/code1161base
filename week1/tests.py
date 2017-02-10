from __future__ import division, print_function
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-5])
from codeHelpers import test

WEEK_NUMBER = 1

# the context of this file
LOCAL = os.path.dirname(os.path.realpath(__file__))
# The curent working directory
CWD = os.getcwd()


def isThereAnID(path_to_code_to_check):
    try:
        place = os.path.join(path_to_code_to_check, '_checkID')
        # print("looking in {}".format(place))
        # print("LOCAL", LOCAL, "\nCWD", CWD)
        f = open(place, 'r')
        contents = f.read()
        # print("contents", contents)
        return len(contents) > 8
    except:
        print("TIP: Have you run pytest.py yet?")
        return False


def isRequestsWorking(path_to_code_to_check):
    try:
        f = open(os.path.join(path_to_code_to_check, '_requestsWorking'), 'r')
        contents = f.read()
        if "noodly appendage" in "".join(contents):
            return True
        elif "Alas, all is lost" in "".join(contents):
            print("looks like your internet connection isn't working")
            return False
        else:
            print("Something strange is happening")
            return False
    except:
        print("TIP: Have you run pytest.py yet?")
        return False


def theTests(path_to_code_to_check=""):
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("Let's check that everything is set up.\n")

    testResults = []
    testResults.append(
        test(isThereAnID(path_to_code_to_check),
             "Exercise 1: Test that your VM is working"))
    testResults.append(
        test(isRequestsWorking(path_to_code_to_check),
             "Exercise 1: Test your connection to the internet"))

    return {"of_total": sum(testResults), "mark": len(testResults)}


if __name__ == "__main__":
    theTests()
