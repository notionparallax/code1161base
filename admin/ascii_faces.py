# -*- coding: UTF-8 -*-
"""Make a page of faces with names.

Run this and it will produce an HTML file with links to everyone's mugshots
"""

from __future__ import division
from __future__ import print_function
import os

LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
# print("LOCAL", LOCAL)
# print("CWD", CWD)

rootdir = '../code1161StudentRepos'


def make_ascii_faces():
    """Generate code for each person."""
    dirList = os.listdir(rootdir)

    for student_repo in dirList:
        try:
            command = "image-to-ascii -i"
            save_location = "./faces/" + student_repo
            path = os.path.join(rootdir, student_repo, "mugshot.png")
            full_command = "{} {} > {}".format(command, path, save_location)
            os.system(full_command)
            print(full_command)
        except Exception as e:
            print(student_repo, e)

make_ascii_faces()
