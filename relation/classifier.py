import kindred
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
import itertools

Corpus = kindred.load(dataFormat='json',path='db/1')
Corpus2 = kindred.load(dataFormat='json',path='db/4')

avg_svm = 0
avg_dct = 0
avg_nn = 0

print("-------------3 CLASSES------------")

iter_count = 1

while iter_count <= 1000:

	trainCorpus,devCorpus = Corpus2.split(trainFraction=0.9)

	predictionCorpus = devCorpus.clone()
	predictionCorpus.removeRelations()

	print("-------"+str(iter_count)+"-------")

	predictionCorpus = devCorpus.clone()
	predictionCorpus.removeRelations()

	classifier = kindred.RelationClassifier()
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	svmf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
	print("svm: ", svmf1score)	
	avg_svm = avg_svm+svmf1score

	classifier = kindred.RelationClassifier(classifierType='DCT')
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	dctf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
	print("dct ",dctf1score)	
	avg_dct = avg_dct+dctf1score

	classifier = kindred.RelationClassifier(classifierType='NN')
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	nnf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
	print("neural networks: ", nnf1score)	
	avg_nn = avg_nn+nnf1score

	iter_count += 1

print("average of SVM:", avg_svm/1000)
print("average of Decision Tree:", avg_dct/1000)
print("average of Neural Networks:", avg_nn/1000)


avg_svm = 0
avg_dct = 0
avg_nn = 0

print("-------------5 CLASSES------------")

iter_count = 1

while iter_count <= 1000:

	trainCorpus,devCorpus = Corpus.split(trainFraction=0.9)

	predictionCorpus = devCorpus.clone()
	predictionCorpus.removeRelations()

	print("-------"+str(iter_count)+"-------")

	predictionCorpus = devCorpus.clone()
	predictionCorpus.removeRelations()

	classifier = kindred.RelationClassifier()
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	svmf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
	print("svm: ", svmf1score)	
	avg_svm = avg_svm+svmf1score

	classifier = kindred.RelationClassifier(classifierType='DCT')
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	dctf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
	print("dct ",dctf1score)	
	avg_dct = avg_dct+dctf1score

	classifier = kindred.RelationClassifier(classifierType='NN')
	classifier.train(trainCorpus)
	classifier.predict(predictionCorpus)
	nnf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
	print("neural networks: ", nnf1score)	
	avg_nn = avg_nn+nnf1score

	iter_count += 1

print("average of SVM:", avg_svm/1000)
print("average of Decision Tree:", avg_dct/1000)
print("average of Neural Networks:", avg_nn/1000)