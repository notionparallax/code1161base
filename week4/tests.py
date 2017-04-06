# -*- coding: UTF-8 -*-
"""Week 4 tests.

This file tests your code. It'll check that the work in each
of the exercise files does what it's supposed to.
"""

from __future__ import division
from __future__ import print_function
import imp
import math
import os
import requests
import sys
import time
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from codeHelpers import completion_message
from codeHelpers import nyan_cat
from codeHelpers import test
from codeHelpers import test_flake8
# from codeHelpers import Timeout

WEEK_NUMBER = 4
LOCAL = os.path.dirname(os.path.realpath(__file__))


def process_wunderground(json_object):
    """Round down wunderground data to make comparison more stable."""
    json_object['latitude'] = math.floor(float(json_object['latitude']))
    json_object['longitude'] = math.floor(float(json_object['longitude']))
    return json_object


def find_lasers(path):
    """Look for a file that contains only the number 6."""
    path = path + "/week4/lasers.pew"
    if os.path.isfile(path):
        return int(open(path).read()) == int(6)
    else:
        print("can't find lasers.pew, did you make it?"
              " Does it have exactly that file name?"
              "looking in " + path)
        return False


def tzOffset():
    """Return tz in hours for current locale."""
    ts = time.time()
    utc_offset = (datetime.fromtimestamp(ts) -
                  datetime.utcfromtimestamp(ts)).total_seconds()
    seconds_in_hour = 60 * 60
    return utc_offset / seconds_in_hour


def treat():
    """Go and get the coloured ascii face particular to this person."""
    url = ("https://raw.githubusercontent.com/"
           "notionparallax/code1161base/master/faces/")

    with open('.git/config', 'r') as f:
        for line in f:
            if ('url = https://github.com/' in line) \
               and not ('notionparallax' in line):
                # ensure it's not Ben's repo
                name = line.split('/')[-2]
                if 'git' in name:
                    # if ssh url
                    name = name.split(':')[-1]
            elif 'url = https://github.com/notionparallax' in line:
                print("we must be testing the tests")
                name = "notionparallax"
    if not name:
        print("Error with getting github username")
    else:
        print("treat:\n", requests.get(url + name).text)


def theTests(path_to_code_to_check="."):
    """Run the tests."""
    print("\nWelcome to week {}!".format(WEEK_NUMBER))
    print("May the odds be ever in your favour.\n")

    path = "{}/week{}/exercise1.py".format(path_to_code_to_check, WEEK_NUMBER)
    print(path)

    exercise1 = imp.load_source("exercise1", path)

    testResults = []

    # stack the tests below here

    print("Linter test:", path)
    testResults.append(
        test(test_flake8(path),
             "Exercise 1: pass the linter"))
    print("tr ", testResults)
    message = '{"message": "Python and requests are working!"}'
    testResults.append(
        test(exercise1.success_is_relative() == message,
             "Exercise 1: read a file using a relative path"))

    testDict = {'lastName': u'hoogmoed',
                'password': u'jokers',
                'postcodePlusID': 4311240}
    testResults.append(
        test(exercise1.get_some_details() == testDict,
             "Exercise 1: get some data out of a JSON file"))

    lengths = [3, 5, 7, 9, 11, 13, 15, 17, 19, 20,
               18, 16, 14, 12, 10, 8, 6, 4]
    try:
        testResults.append(
            test([len(w) for w in exercise1.wordy_pyramid()] == lengths,
                 "Exercise 1: request some simple data from the internet"))
    except Exception as e:
        testResults.append(0)
        print("Exercise 1: request some simple data from the internet", e)

    weather_results = {'latitude': u'-33.924206',
                       'state': u'NSW',
                       'longitude': u'151.187912',
                       'local_tz_offset': u'+{}00'.format(int(tzOffset()))}
    try:
        ex_name = "Exercise 1: get some data from the weather underground."
        theirs = process_wunderground(exercise1.wunderground())
        mine = process_wunderground(weather_results)
        print("you gave:", theirs)
        print("expected:", mine)
        testResults.append(
            test(theirs == mine, ex_name))
    except Exception as e:
        testResults.append(0)
        print(ex_name, e)

    testResults.append(
            test(find_lasers(path_to_code_to_check),
                 "Exercise 1: count the lasers."))

    print("{0}/{1} (passed/attempted)".format(sum(testResults),
                                              len(testResults)))

    if sum(testResults) == len(testResults):
        nyan_cat()
        message = "Rad, you've got all the tests passing!"
        completion_message(message, len(message) + 2)
        treat()

    return {"of_total": len(testResults),
            "mark": sum(testResults),
            "results": testResults}


if __name__ == "__main__":
    theTests()
