import kindred
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
import itertools


Corpus = kindred.load(dataFormat='json',path='db/1')
Corpus2 = kindred.load(dataFormat='json',path='db/4')

fList = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]
average = 0

print("-------------3 CLASSES------------")
for i in fList:
	trainCorpus,devCorpus = Corpus2.split(trainFraction=i)

	predictionCorpus = devCorpus.clone()
	predictionCorpus.removeRelations()

	classifier = kindred.RelationClassifier()
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
	print(i, f1score)	
	average = average+f1score



print("average:", average/len(fList))

average = 0
print("-------------5 CLASSES------------")
for i in fList:
	trainCorpus,devCorpus = Corpus.split(trainFraction=i)

	predictionCorpus = devCorpus.clone()
	predictionCorpus.removeRelations()

	classifier = kindred.RelationClassifier()
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
	print(i, f1score)
	average = average+f1score

	classifier = kindred.RelationClassifier(classifierType='DCT')
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	svmf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
	print(i, f1score)	
	average = average+f1score

	classifier = kindred.RelationClassifier(classifierType='NN')
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	svmf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
	print(i, f1score)	
	average = average+f1score
print("average:", average/len(fList))

