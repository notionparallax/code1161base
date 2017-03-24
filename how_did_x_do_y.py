# -*- coding: UTF-8 -*-
"""Run a lightweight test set on specific students."""
import os
import subprocess

LOCAL = os.path.dirname(os.path.realpath(__file__))
week_number = 2
exercise_number = 3


repos = ["Rizo007", "pennypangCODE", "FlimEden", "sheldakristie", "RangoRay",
         "lorniashi", "atiredturtle", "alanw410", "Matchalism", "TerryAg",
         "sherry0303", "AkisukeY", "872815554", "dbisazza", "timtamtinyman999",
         "DarkPurple141", "zingjanet", "tomwyb", "matthewpoytress",
         "BaptisteHiggs", "DanielHeh", "OneMoreN"]

results = []
for name in repos:
    path = "/{}/week{}/exercise{}.py".format(name,
                                             week_number,
                                             exercise_number)
    subprocess.call(['python',
                     './inspector_shim.py',
                     "",
                     "../code1161StudentRepos" + path])
    temp_results = open(os.path.join(LOCAL, 'temp_inspect.json'), 'r')
    results.append({"name": name, "code": temp_results.read()})
    temp_results.close()

print repr(results)
