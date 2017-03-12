# -*- coding: UTF-8 -*-
"""Make a page of faces with names.

Run this and it will produce an HTML file with links to everyone's mugshots
"""

from __future__ import division
from __future__ import print_function
import os
import ruamel.yaml as yaml

# from week1.tests import theTests as w1test
from importlib import import_module
WEEK_NUMBER = 1
w1test = import_module("week{}.tests".format(WEEK_NUMBER), "theTests")
w1test = w1test.theTests

LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
# print("LOCAL", LOCAL)
# print("CWD", CWD)

rootdir = '../code1161StudentRepos'


def the_style():
    """"Return the css.

    Just keeps things tidy.
    """
    return """
    <style>
    .person {
        display: inline-block;
        height: 30em;
        overflow: hidden;
        position: relative;
        width: 20em;
    }
    .person img {
        object-fit: cover;
        width: 100%;
    }
    .person h1, .person dl {
      background: hsla(0, 0%, 100%, 0.5);
      display: inline-block;
      margin: 0;
      position: absolute;
    }
    .person h1 {
      top: 0;
      padding: 0 1em;
    }
    .person dl {
      bottom: 0;
      font-size: 85%;
    }
    dt, dd {
        display: inline;
        padding: 0;
        margin: 0 0.1em;
    }
    dt {
        font-weight: bold;
    }
    </style>
    """


def make_guess_who_board():
    """Generate code for each person."""
    dirList = os.listdir(rootdir)

    body = the_style()

    for student_repo in dirList:
        try:
            path = os.path.join(rootdir, student_repo, "aboutMe.yml")
            details = open(path).read()
            details = details.replace("@", "^AT^")
            details = details.replace("é", "e")
            details = details.replace(":([^ /])", ": $1")
            details = yaml.load(details, yaml.RoundTripLoader)
            if details["mediumUsername"][0] != "@":
                details["mediumUsername"] = "@" + details["mediumUsername"]
            details["repo_name"] = student_repo
            print(details)
            body += """
            <div class="person">
            <img src="https://raw.githubusercontent.com/{gitHubUsername}/code1161base/master/mugshot.png">
            <h1>{name}</h1>
            <dl>
            <dt>name:</dt>
              <dd>{name}</dd>
            <dt>Student Number:</dt>
              <dd>{studentNumber}</dd>
            <dt>GitHub:</dt>
              <dd>
                <a href="https://github.com/{gitHubUsername}">{gitHubUsername}</a>
              </dd>
            <dt>Stackoverflow:</dt>
              <dd>
                <a href="{stackoverflow}">{stackoverflow}</a>
              </dd>
            <dt>Medium:</dt>
              <dd>
                <a href="https://medium.com/{mediumUsername}">{mediumUsername}</a>
              </dd>
            <dt>UNSW Email:</dt>
              <dd>{unswEmail}</dd>
            <dt>realEmail:</dt>
              <dd>{realEmailFirstBit}{realEmailOtherBit}</dd>
            </dl>
            </div>""".format(**details).replace("^AT^", "@")
        except Exception as e:
            print("failed on", student_repo, e)
    return body


target = open("guess_who_poster.html", 'w')
target.write(make_guess_who_board())
target.close()
