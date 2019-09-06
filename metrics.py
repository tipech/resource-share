

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

scores = []

for intersection in intersections["results"]["regions"]:

	width = intersection["dimensions"][0][1]-intersection["dimensions"][0][0]
	height = intersection["dimensions"][1][1]-intersection["dimensions"][1][0]

	resource = 0
	for user in intersection["data"]["intersect"]:
		resource += regions[user]["data"]["resources"][0]["value"]

	ranking = {
		"units": resource,
		"count": len(intersection["data"]["intersect"]),
		"area": width * height
	}

	res_factor = 1
	count_factor = .5
	area_factor = .5

	ranking["score"] = ( 
		res_factor * ranking["units"] 
		+ count_factor * ranking["count"]
		+ area_factor * ranking["area"])

	intersection["ranking"] = ranking

	scores.append( (intersection["id"], ranking["score"]) )


scores = sorted(scores, key=lambda x: x[1], reverse=True)
scores = scores[:100]

pprint(scores)


with open('data/final.json', 'w') as final:
    final.write( json.dumps(intersections, sort_keys=True,
				indent=4, separators=(',', ': ')))

