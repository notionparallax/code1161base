# -*- coding: UTF-8 -*-
import sys
import inspect
import imp
import os

REPO_PATH = sys.argv[2]
LOCAL = os.path.dirname(os.path.realpath(__file__))


def do_the_test():
    try:
        test = imp.load_source("test", REPO_PATH)
        r = inspect.getsourcelines(test.loops_7)
        return str(r)
    except Exception as e:
        print e


temp_results = open('temp_inspect.json', 'w')
temp_results.write(do_the_test())
temp_results.close()
