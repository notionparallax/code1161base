# -*- coding: UTF-8 -*-
import requests
import json

# writerNames = ["kmatthews25", "lachlan.benjamin.brown", "pennypang.t", "guy_segev", "williambackman12", "marcosbbc", "levin.chen888", "Sunsadymark", "hannah.lazenby1", "baptistehiggs", "thuvab", "wilham77", "mcfblair", "lisa.doan2625", "alexlewis20", "AkisukeY", "sudassanap", "alainchen", "sherry0303", "richardwhitfield_55841", "shawnee.finlayson", "annisar.rizal", "chrischidiac", "Zingjanet", "meng.lei086", "joseangelodiaz", "shelda.kristie", "xavier.nuttall", "ethangonzaga", "lorniashi", "tomwyb", "catherine.vu.97", "cx459594334", "jamesbui888", "navkaranvirdi", "cdyl.darrellchan", "harley.t", "terry_28421", "daniel_heh", "ishaan.varshney", "potatobeees", "timtamtinyman999", "Ravionf", "jeremysaguinsin", "williambackman", "kongwukai", "danielle.bisazza", "liumuyang040431", "s.bojceska", "al_hinds", "cahetti", "mikaliuyuncong", "nblucchese", "joshcoady", "flim.edenli", "chendujiang98", "matthewpoytress33", "addycap", "JayChen980919", "m.waldo014", "alain.chyn", "stephen.karahalias", "charlottecui", "michaelrizoski", "alanw410", "caroline120248", "matthewpaulmcelroy", "linseenlee", "christopheryip_221"]

r = requests.get("https://medium.com/code17?format=json")
data = json.loads(r.text.encode('utf-8')[16:])
users = data["payload"]["references"]["User"]
posts = data["payload"]["references"]["Post"]

usernames = {}
for k in users.keys():
    us = users[k]
    usernames[us["userId"]] = {"username": us["username"].encode('utf8'),
                               "name": us["name"].encode('utf8')}
    template = u"{username}, {name}, {userId}"
    print template.format(**us).encode('utf8')

for k in posts.keys():
    p = posts[k]

    tidyD = {}
    tidyD["title"] = p["title"].strip()
    tidyD["username"] = usernames[p["creatorId"]]["username"]
    tidyD["name"] = usernames[p["creatorId"]]["name"].decode('utf-8')
    tidyD["creatorId"] = p["creatorId"]
    tidyD["firstPublishedAt"] = p["firstPublishedAt"]
    # print tidyD
    template = (u"{title}, "
                u"author: {username} - {name} ({creatorId}), "
                u"pub Date {firstPublishedAt}")
    details = template.format(**tidyD)
    print details.encode('utf-8')
