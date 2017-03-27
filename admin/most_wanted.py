# -*- coding: UTF-8 -*-
"""Make a page of faces with names.

Run this and it will produce an HTML file with links to everyone's mugshots
"""

from __future__ import division
from __future__ import print_function
from importlib import import_module
from StringIO import StringIO
import os
import pandas as pd
import requests
import ruamel.yaml as yaml


LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
# print("LOCAL", LOCAL)
# print("CWD", CWD)

rootdir = '../code1161StudentRepos'


def the_head():
    """"Return the css.

    Just keeps things tidy.
    """
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Python Adventurers</title>
        <link rel="stylesheet" href="admin/mugshot.css">
        <script src="script.js"></script>
      </head>
      <body>
    """


def card_template(details):
    details["raw"] = "https://raw.githubusercontent.com"
    details["gh"] = "https://github.com"
    details["medium"] = "https://medium.com"
    return """
    <div class="person">
    <img src="{raw}/{gitHubUsername}/{repo_name}/master/mugshot.png">
    <h1>{name}</h1>
    <dl>
    <dt>name:</dt>
      <dd>{name}</dd>
    <dt>Student Number:</dt>
      <dd>{studentNumber}</dd>
    <dt>GitHub:</dt>
      <dd>
        <a href="{gh}/{gitHubUsername}/{repo_name}">{gitHubUsername}</a>
      </dd>
    <dt>Stackoverflow:</dt>
      <dd>
        <a href="{stackoverflow}">{stackoverflow}</a>
      </dd>
    <dt>Medium:</dt>
      <dd>
        <a href="{medium}/{mediumUsername}">{mediumUsername}</a>
      </dd>
    <dt>UNSW Email:</dt>
      <dd>{unswEmail}</dd>
    <dt>realEmail:</dt>
      <dd>{realEmailFirstBit}{realEmailOtherBit}</dd>
    <dt>slack:</dt>
      <dd>{slack}</dd>
    </dl>
    </div>""".format(**details).replace("^AT^", "@")


def getDFfromCSVURL(url, columnNames=False):
    """Get a csv of values from google docs."""
    r = requests.get(url)
    data = r.content
    if columnNames:
        return pd.read_csv(StringIO(data), header=0, names=columnNames)
    else:
        return pd.read_csv(StringIO(data))


def df_of_students():
    """Get an updated copy of the spreadsheet."""
    # pull the forks list
    ss_of_details_url = ("https://docs.google.com/spreadsheets/d/"
                         "1qeOp6PZ48BFLlHaH3ZEil09MBNfQD0gztuCm2cEiyOo/"
                         "pub?gid=2144767463"
                         "&single=true&output=csv")

    return getDFfromCSVURL(ss_of_details_url, ["paste",
                                               "their_username",
                                               "repo_name",
                                               "check",
                                               "repo_url",
                                               "slack"])


def rip_out_dicts(d):
    newD = {}
    for key in d.iterkeys():
        row = d[key]
        if type(row) is dict:
            i = row.keys()[0]
            newD[key] = row[i]
        else:
            newD[key] = row
    return newD


def graft_fork_onto_aboutMe(forkDetails, about_me_details):
    f = forkDetails
    a = dict(about_me_details)
    # print("XXXXXXXXXX", f, "\n", a)
    username = a["gitHubUsername"]

    def safe_lower(x):
        return str(x).upper().lower()

    pertinent_row = f[f["their_username"].apply(safe_lower) ==
                      safe_lower(username)]
    # print("pertinent_row", pertinent_row)
    try:
        pertinent_row = pertinent_row.to_dict()
        a.update(pertinent_row)  # update is in place
        return rip_out_dicts(a)
    except:
        pass  # print(username, pertinent_row)


def make_guess_who_board():
    """Generate code for each person."""
    dirList = os.listdir(rootdir)

    student_fork_details = df_of_students()

    body = the_head()

    for student_repo in dirList:
        path = os.path.join(rootdir, student_repo, "aboutMe.yml")
        details = open(path).read()
        details = details.replace("@", "^AT^")
        details = details.replace("é", "e")
        details = details.replace(":([^ /])", ": $1")
        details = yaml.load(details, yaml.RoundTripLoader)
        if details["mediumUsername"][0] != "@":
            details["mediumUsername"] = "@" + details["mediumUsername"]
        details["repo_name"] = student_repo
        details = graft_fork_onto_aboutMe(student_fork_details,
                                          details)
        # print(details)
        try:
            body += card_template(details)
        except:
            pass

    return body + "</body></html>"


target = open("guess_who_poster.html", 'w')
target.write(make_guess_who_board())
target.close()
