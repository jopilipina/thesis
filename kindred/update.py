import os
import json
from collections import OrderedDict

FOLDER = "db/7525/train/"
NEW = "db/new/train/"

for file in os.listdir(FOLDER):
	# print(file)
	with open(FOLDER + file, "r") as json_file:
		data = json.load(json_file, object_pairs_hook=OrderedDict)
		for i in data["denotations"]:
			# print(i["span"])
			d = i["span"]
			x = d["end"]+1
			d2 = {"end": x}
			d.update(d2)
	newdir = NEW + file
	if not os.path.exists(os.path.dirname(newdir)):
		os.makedirs(os.path.dirname(newdir))
	with open(newdir, "w") as json_new:
		json_new.write(json.dumps(data, indent = 4))