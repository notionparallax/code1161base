# -*- coding: UTF-8 -*-
from importlib import import_module
import json
import sys

TEST_PATH = sys.argv[1]
REPO_PATH = sys.argv[2]


def do_the_test():
    try:
        test = import_module(TEST_PATH, package="code1161base")
        r = test.theTests(REPO_PATH)
        r["localError"] = ":)"
        return r
    except Exception as e:
        return {"of_total": 0,
                "mark": 0,
                "localError": str(e).replace(",", "~").encode('utf-8')}
        # the comma messes with the csv


def results_as_json():
    results = do_the_test()
    results["name"] = REPO_PATH.split("/")[-1]
    return json.dumps(results)


temp_results = open('temp_results.json', 'w')
temp_results.write(results_as_json())
temp_results.close()
