# -*- coding: UTF-8 -*-
"""Get the latest copy of all the repos.

This pulls the latest copy of all the repos
It can clone new repos if you set THERE_ARE_NEW_STUDENTS to true
"""

from __future__ import division
from __future__ import print_function
from StringIO import StringIO
import git
import os
import pandas as pd
import requests
import subprocess
import json


LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
print("LOCAL", LOCAL)
print("CWD", CWD)


def getDFfromCSVURL(url, columnNames=False):
    """Get a csv of values from google docs."""
    r = requests.get(url)
    data = r.content
    if columnNames:
        return pd.read_csv(StringIO(data), header=0, names=columnNames)
    else:
        return pd.read_csv(StringIO(data))


def update_for_new_students(chatty=False):
    """Get an updated copy of the spreadsheet."""
    # pull the forks list
    ss_of_details_url = ("https://docs.google.com/spreadsheets/d/"
                         "1qeOp6PZ48BFLlHaH3ZEil09MBNfQD0gztuCm2cEiyOo/"
                         "pub?gid=2144767463"
                         "&single=true&output=csv")

    student_details = getDFfromCSVURL(ss_of_details_url, ["paste",
                                                          "their_username",
                                                          "repo_name",
                                                          "check",
                                                          "repo_url",
                                                          "slack"])

    for index, student in student_details.iterrows():
        try:
            git.Repo.clone_from(student.repo_url,
                                os.path.join(rootdir, student.their_username))
            print("new repo for", student.their_username)
        except Exception:
            if chatty:
                print("we already have", student.their_username)

    return student_details


def pull_all_repos(dirList):
    """Pull latest version of all repos."""
    for student_repo in dirList:
        git.cmd.Git(os.path.join(rootdir, student_repo)).pull()


def csvOfDetails(dirList):
    """Make a CSV of all the students."""
    import ruamel.yaml as yaml
    results = []
    for student_repo in dirList:
        try:
            path = os.path.join(rootdir, student_repo, "aboutMe.yml")
            details = open(path).read()
            details = details.replace("@", "^AT^")
            details = details.replace("é", "e")
            details = details.replace("w:", "w: ")
            details = yaml.load(details, yaml.RoundTripLoader)
            details["repoName"] = student_repo
            details["error"] = False
            if details["mediumUsername"][:4] != "^AT^":
                details["mediumUsername"] = "^AT^" + details["mediumUsername"]
            results.append(details)

            if details["studentNumber"] == "z1234567":
                print(student_repo, "hasn't updated")
        except Exception as e:
            results.append({'error': e, "repoName": student_repo})

    print("\n\nResults:")
    resultsDF = pd.DataFrame(results)
    # print(resultsDF)
    resultsDF.to_csv(os.path.join(CWD, "csv/studentDetails.csv"))
    fix_up_csv()


def fix_up_csv(path="csv/studentDetails.csv"):
    lines = []
    with open(path) as infile:
        for line in infile:
            line = line.replace("^AT^", "@")
            line = line.replace(",,", ",-,")
            lines.append(line)
    with open(path, 'w') as outfile:
        for line in lines:
            print(line)
            outfile.write(line)


def mark_work(dirList, week_number, root_dir):
    """Mark the week's exercises."""
    results = []
    for student_repo in dirList:
        try:
            subprocess.call(['python',
                             './test_shim.py',
                             "week{}.tests".format(week_number),
                             "{}/{}".format(root_dir, student_repo)])

            temp_results = open(os.path.join(LOCAL, 'temp_results.json'), 'r')
            results_dict = json.loads(temp_results.read())
            results_dict["bigerror"] = ":)"
            results.append(results_dict)
            temp_results.close()
        except Exception as e:
            results.append({"bigerror": str(e).replace(",", "~"),
                            "name": student_repo})
            # the comma messes with the csv

    resultsDF = pd.DataFrame(results)
    print("\n\nResults:\n", resultsDF)
    resultsDF.to_csv(os.path.join(CWD,
                                  "csv/week{}marks.csv".format(week_number)),
                     index=False)
    print("\n+-+-+-+-+-+-+-+")
    return resultsDF


rootdir = '../code1161StudentRepos'

dirList = os.listdir(rootdir)
print("dir list", dirList)

print("\nCheck to see if there are any new students in the spreadsheet")
update_for_new_students(chatty=True)

print("\nPull all the repos so we have the latest copy. (This takes a while.)")
pull_all_repos(dirList)

print("\nUpdate the CSV of details")
csvOfDetails(dirList)
# This feeds the sanity check spreadsheet

print("\nMark week 1's work")
mark_work(dirList, 1, rootdir)

print("\nMark week 2's work")
mark_work(dirList, 2, rootdir)

print("\nMark week 3's work")
mark_work(dirList, 3, rootdir)

print("\nMark week 4's work")
mark_work(dirList, 4, rootdir)
