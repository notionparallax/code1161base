# -*- coding: UTF-8 -*-
"""Run a lightweight test set on specific students."""
import os
from codeHelpers import RunCmd

LOCAL = os.path.dirname(os.path.realpath(__file__))
week_number = 4


repos = ["code1161benFork_fully_working_secret_squirel"]
results = []
for name in repos:
    try:
        timeout_cap = 5
        args = ['python',
                './test_shim.py',
                "week{}.tests".format(week_number),
                "../code1161StudentRepos/{}".format(name)]
        RunCmd(args, timeout_cap).Run()

        temp_results = open(os.path.join(LOCAL, 'temp_results.json'), 'r')
        results.append(temp_results.read())
        temp_results.close()
    except Exception as e:
        print e

print results
