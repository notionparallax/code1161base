# -*- coding: UTF-8 -*-
"""Get the latest version of the tests.

Goes to github and downloads the tests.
"""
import os
import requests

LOCAL = os.path.dirname(os.path.realpath(__file__))
# print(LOCAL)


def get_the_updates():
    gh_url = 'https://raw.githubusercontent.com/'
    repo = 'notionparallax/code1161base/'
    for i in [1, 2, 3, 4, 5, 6, 8]:  # no week 7
        file_path = "master/week{}/tests.py".format(i)
        url = gh_url + repo + file_path
        save_path = "week{}/tests.py".format(i)
        download_and_save(url, save_path)
    download_and_save(gh_url + repo + "master/codeHelpers.py",
                      "codeHelpers.py")


def get_file_text(url):
    r = requests.get(url)
    return r.text.encode('utf-8')


def download_and_save(url, save_path):
    f = open(os.path.join(LOCAL, save_path), 'w')
    f.write(get_file_text(url))
    f.close()


get_the_updates()
print "Fingers crossed! Try the tests for week 3 now"
print "Remember: the changes to the tests will need to be commited"
print "          as well as your work."
