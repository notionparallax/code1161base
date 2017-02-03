import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-5])
from codeHelpers import test


def isThereAnID():
    try:
        f = open('_checkID', 'r')
        contents = f.read()
        print contents
        return len(contents) > 8
    except:
        print "TIP: Have you run pytest.py yet?"
        return False


def isRequestsWorking():
    try:
        f = open('_requestsWorking', 'r')
        contents = f.read()
        if "noodly appendage" in "".join(contents):
            return True
        elif "Alas, all is lost" in "".join(contents):
            print "looks like your internet connection isn't working"
            return False
        else:
            print "Something strange is happening"
            return False
    except:
        print "TIP: Have you run pytest.py yet?"
        return False


print "\nWelcome to week 1!\nLet's check that everything is set up.\n"

test(isThereAnID(), "Exercise 1: Test that your VM is working")
test(isRequestsWorking(), "Exercise 1: Test your connection to the internet")
