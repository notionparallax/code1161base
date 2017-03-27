"""Do the work of checking the week's work."""
from __future__ import division
from __future__ import print_function
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import test

WEEK_NUMBER = 1

# the context of this file
LOCAL = os.path.dirname(os.path.realpath(__file__))
# The curent working directory
CWD = os.getcwd()


def isThereAnID(path_to_code_to_check):
    """Check that this test is being run on a VM."""
    try:
        place = os.path.join(path_to_code_to_check, '_checkID')
        print("looking in {}".format(place))
        print("LOCAL", LOCAL, "\nCWD", CWD)
        f = open(place, 'r')
        contents = f.read()
        print("contents", contents)
        return len(contents) > 8
    except Exception:
        print("TIP: Have you run pytest.py yet?")
        return False


def isRequestsWorking(path_to_code_to_check):
    """Check that the requests library is installed and working.

    This makes a request from a web location so it also checks that the VM is
    connected to the internet.

    """
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
    except Exception:
        print("TIP: Have you run pytest.py yet?")
        return False


def theTests(path_to_code_to_check="."):
    """Run the tests.

    This is the main function, it contains all the tests for the week.
    """
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("Let's check that everything is set up.\n")

    path = "{}/week{}/".format(path_to_code_to_check, WEEK_NUMBER)
    testResults = []
    testResults.append(
        test(isThereAnID(path),
             "Exercise 1: Test that your VM is working"))
    testResults.append(
        test(isRequestsWorking(path),
             "Exercise 1: Test your connection to the internet"))

    return {"of_total": len(testResults),
            "mark": sum(testResults),
            "results": testResults}


if __name__ == "__main__":
    theTests()
