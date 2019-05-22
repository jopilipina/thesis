import csv

text_file = open("h.txt", "r")
line = "1"

with text_file as fp:  
	with open('masterlist_5types.csv', mode='w') as csv_file:
		fieldnames = ['svm', 'decision_trees', 'neural_net']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		while line:
			writer.writerow({'svm': fp.readline().strip(), 'decision_trees': fp.readline().strip(), 'neural_net': fp.readline().strip()})
			line = fp.readline()
