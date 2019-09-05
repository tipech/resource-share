

import json
from pprint import pprint


regions = {}
intersections = {}

with open("data/input.json") as regions_file:
	regions_dict = json.load(regions_file)

	for region in regions_dict["regions"]:
		regions[region["id"]] = region


with open("data/output.json") as intersections_file:
	intersections = json.load(intersections_file)

for intersection in intersections["results"]["regions"]:

	resource = 0
	for user in intersection["data"]["intersect"]:
		print(regions[user]["data"]["resources"])
