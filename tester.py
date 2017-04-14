# -*- coding: UTF-8 -*-
"""Run a lightweight test set on specific students."""
from codeHelpers import RunCmd
import os
import time

LOCAL = os.path.dirname(os.path.realpath(__file__))
week_number = 4


repos = ["code1161benFork_fully_working_secret_squirel"]
times = []
repos = ["alanw410", "bvn-architecture","alanw410", "bvn-architecture","alanw410", "bvn-architecture","alanw410", "bvn-architecture","alanw410", "bvn-architecture"]  # "bvn-architecture"
results = []
for name in repos:
    start_time = time.time()
    try:
        timeout_cap = 25
        args = ['python',
                './test_shim.py',
                "week{}.tests".format(week_number),
                "../code1161StudentRepos/{}".format(name)]
        print args
        RunCmd(args, timeout_cap).Run()

        temp_results = open(os.path.join(LOCAL, 'temp_results.json'), 'r')
        results.append(temp_results.read())
        temp_results.close()
    except Exception as e:
        print e
    elapsed_time = time.time() - start_time
    print "Time to test:", elapsed_time
    times.append({"name": name, "time": elapsed_time})

print results
print times
