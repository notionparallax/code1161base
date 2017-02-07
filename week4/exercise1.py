"""
Docstring
"""
import requests
import json
import os

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print "Be careful that your relative paths are"
    print "relative to where you think they are"
    print LOCAL
    print CWD


def get_some_details():
    """
    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()

    data = json.loads(json_data)
    return {"lastName": data["results"][0]["name"]["last"],
            "password": data["results"][0]["login"]["password"],
            "postcodePlusID": data["results"][0]["location"]["postcode"] +
            int(data["results"][0]["id"]["value"])
            }
    # TODO: leave this as is but change the dict to key:None


def wordy_pyramid():
    """
    There is a random word generator here: http://www.setgetgo.com/randomword/
    The only argument that the generator takes is the length of the word.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. ?len=
    """
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


def json_in_a_van():
    """
    Get some json from a request
    parse it and extract values
    """


def diarist():
    """
    write some data to a file
    """


def finding_the_gcode():
    """
    Parse a file, find the lines that contain a certain
    value - gcode maybe?
    """


if __name__ == "__main__":
    print [len(w) for w in wordy_pyramid()]
    print get_some_details()
