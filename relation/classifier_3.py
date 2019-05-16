import kindred
import argparse
import os
import csv

# trainCorpus = kindred.load(dataFormat='json',path='db/2/train')
# devCorpus = kindred.load(dataFormat='json',path='db/2/train/')

with open('three_types.csv', mode='w') as csv_file:
	fieldnames = ['iteration_num', 'svm', 'decision_trees', 'neural_net']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

	writer.writeheader()

	Corpus = kindred.load(dataFormat='json',path='db/4')

	avg_svm = 0
	avg_dct = 0
	avg_nn = 0

	count = 0
	iter_num = 5

	print("-------------3 CLASSES------------")

	while count < iter_num:
		trainCorpus,devCorpus = Corpus.split(trainFraction=0.9)

		predictionCorpus = devCorpus.clone()
		predictionCorpus.removeRelations()

		classifier = kindred.RelationClassifier()
		classifier.train(trainCorpus)
		classifier.predict(predictionCorpus)
		svmf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
		print("svm:\t", svmf1score)

		avg_svm = avg_svm+svmf1score

		classifier = kindred.RelationClassifier(classifierType='DCT')
		classifier.train(trainCorpus)
		classifier.predict(predictionCorpus)
		dctf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
		print("dct:\t", dctf1score)	
		avg_dct = avg_dct+dctf1score

		classifier = kindred.RelationClassifier(classifierType='NN')
		classifier.train(trainCorpus)
		classifier.predict(predictionCorpus)
		nnf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=True)
		print("nn:\t", nnf1score)	
		avg_nn = avg_nn+nnf1score

		writer.writerow({'iteration_num': iter_num, 'svm': svmf1score, 'decision_trees': dctf1score, 'neural_net': nnf1score})

		count += 1

	print("average of SVM:", avg_svm/iter_num)
	print("average of DCT:", avg_dct/iter_num)
	print("average of Neural Networks:", avg_nn/iter_num)


	writer.writerow({'iteration_num': iter_num, 'svm': avg_svm, 'decision_trees': avg_dct, 'neural_net': avg_nn})