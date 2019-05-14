# import kindred
# import argparse
# import os

# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser(description='Use annotated sentences to build a Kindred classifer and apply to unannotated sentences')
# 	parser.add_argument('--dataToBuildModel',required=True,type=str,help='Sentences with relations')
# 	parser.add_argument('--dataToApplyModel',required=True,type=str,help='Sentences without annotated relations to make predictions on')
# 	parser.add_argument('--outDir',required=True,type=str,help='Directory to store output')
# 	args = parser.parse_args()

# 	print("Loading corpora...")
# 	trainCorpus = kindred.load('standoff',args.dataToBuildModel)
# 	predictionCorpus = kindred.load('standoff',args.dataToApplyModel)

# 	print("Building classifier...")
# 	classifier = kindred.RelationClassifier()
# 	classifier.train(trainCorpus)

# 	print("Applying classifier...")
# 	classifier.predict(predictionCorpus)

# 	if not os.path.isdir(args.outDir):
# 		os.makedirs(args.outDir)

# 	print("Saving results to directory...")
# 	kindred.save(predictionCorpus,'standoff',args.outDir)

# 	print("\nPredicted relations:")
# 	for relation in predictionCorpus.getRelations():
# 		print("%s\t%s" % (relation.entities[0].text,relation.entities[1].text))

import kindred
import argparse
import os

trainCorpus = kindred.loadDir(dataFormat='json',directory='db/3/train')
devCorpus = kindred.loadDir(dataFormat='json',directory='db/3/test/')

predictionCorpus = devCorpus.clone()
predictionCorpus.removeRelations()

classifier = kindred.RelationClassifier()
classifier.train(trainCorpus)
classifier.predict(predictionCorpus)

f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
print("Train then Test:", f1score)

# for i in predictionCorpus.getRelations():
#   print(i)

# for i in devCorpus.getRelations():
#   print(i)