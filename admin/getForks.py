import json
import pandas as pd
import requests

url = "https://api.github.com/repos/notionparallax/code1161base/forks"
r = requests.get(url + "?per_page=100")
theJson = json.loads(r.text)


def get_the_useful(j):
    login = j[u"owner"][u'login']
    url = j[u"clone_url"]
    name = j[u"name"]
    return {"login": login, "url": url, "name": name}


deets = [get_the_useful(j) for j in theJson]
print(len(deets))
df = pd.DataFrame(deets)
print("\n\nResults:\n", df)
df.to_csv("csv/github.csv", index=False, columns=["login", "url", "name"])
