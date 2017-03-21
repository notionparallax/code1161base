# ![](https://placekitten.com/900/900)


# -*- coding: UTF-8 -*-
"""Make a markdown file that makes giant slide deck.

targets https://github.com/googlesamples/md2googleslides
"""

from __future__ import division
from __future__ import print_function
from StringIO import StringIO
import os
import pandas as pd
import requests


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
                         "pub?gid=1953197232"
                         "&single=true&output=csv")

    student_details = getDFfromCSVURL(ss_of_details_url,
                                      ["unsw_name",
                                       "gitHubUsername",
                                       "mediumUsername",
                                       "on_medium",
                                       "name",
                                       "realEmailFirstBit",
                                       "realEmailOtherBit",
                                       "gh_username",
                                       "stackoverflow",
                                       "studentNumber",
                                       "unswEmail",
                                       "slack_username",
                                       "h_w_topic",
                                       "nice_email",
                                       "gh_has_fork",
                                       "on_slack",
                                       "repo_name"])

    # print(student_details.head())
    whole_deck = ""
    ignore_list = ["sunsdaymark", "AidenRay", "notionparallax",
                   "ishaanv", "NavkaranVirdi"]

    for index, student in student_details.iterrows():
        if student["gitHubUsername"] not in ignore_list:
            try:
                whole_deck += md_for_this_person(student)
            except Exception as e:
                print(e, student)

    print(whole_deck)


def md_for_this_person(student):
    """Make the MD for one person's slides.

    Example data:
    unsw_name                 Virdi,Navkaran
    gitHubUsername             NavkaranVirdi
    mediumUsername             navkaranvirdi
    on_medium                 @navkaranvirdi
    name                      Navkaran Virdi
    realEmailFirstBit             navkaran95
    realEmailOtherBit             @gmail.com
    gh_username                NavkaranVirdi
    stackoverflow
    studentNumber                   z5015881
    unswEmail        z5015881@ad.unsw.edu.au
    slack_username            @navkaranvirdi
    h_w_topic Pair programming or not?
    nice_email          navkaran95@gmail.com
    gh_has_fork                         True
    on_slack                  @navkaranvirdi
    """
    slide_data = {}
    name = student["unsw_name"].split(",")
    slide_data["name"] = "{} {}".format(name[1], name[0])
    slide_data["topic"] = student["h_w_topic"]
    slide_data["repo"] = student["repo_name"]
    slide_data["ghu"] = student["gitHubUsername"]

    md = """---

# {topic}

## {name}

![](https://raw.githubusercontent.com/{ghu}/{repo}/master/mugshot.png){{.background}}""".format(**slide_data)

    for i in range(1, 5):
        md += """\n---

# {0} {{.big}}

## Explaining what it means\n""".format(i)

    for i in range(5, 15):
        md += """\n---

# {0} {{.big}}

## Going into some detail\n""".format(i)

    for i in range(15, 21):
        md += """\n---

# {0} {{.big}}

## Explaining why you believe what you do\n""".format(i)

    md += """---
![](http://giant.gfycat.com/ElatedGleefulBernesemountaindog.gif)

---

![](http://orig06.deviantart.net/707e/f/2015/129/a/e/incoming_transmission_by_d_elightfullydevious-d8srn7q.gif)
"""
    return md


update_for_new_students()
