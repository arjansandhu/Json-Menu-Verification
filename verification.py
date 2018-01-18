
import json
import urllib2

url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"
print(url)

menu = urllib2.urlopen(url)
menuJson = menu.read()
jsonData = json.loads(menuJson)

pageSize = jsonData["pagination"]["per_page"]
totalSize = jsonData["pagination"]["total"]
nodes = [dict() for x in range(totalSize)]

i = 0
pagesDone = 0
while True:
	for x in range(pageSize):
		nodes[i]["id"] = jsonData["menus"][x]["id"]
		nodes[i]["data"] = jsonData["menus"][x]["data"]
		if "parent_id" in jsonData["menus"][x]:
			nodes[i]["parent_id"] = jsonData["menus"][x]["parent_id"]
		nodes[i]["child_ids"] = jsonData["menus"][x]["child_ids"]
		i = i + 1
	pagesDone = pagesDone + 1

	if(pagesDone*pageSize >= totalSize):
		break;

	url = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=" + `(pagesDone + 1)`
	print(url)
	menu = urllib2.urlopen(url)
	menuJson = menu.read()
	jsonData = json.loads(menuJson)

print nodes

menus = {}

for node in nodes:
	if "parent_id" not in node:
		menus[node["id"]] = []
print(menus)
for node in nodes:
	if node["id"] not in menus:
		menus[node["parent_id"]].append(node["id"])


print(menus)