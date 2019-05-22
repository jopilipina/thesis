import kindred
import argparse
import os
import csv

# trainCorpus = kindred.load(dataFormat='json',path='db/2/train')
# devCorpus = kindred.load(dataFormat='json',path='db/2/train/')

with open('5_types2.csv', mode='w') as csv_file:
	fieldnames = ['iteration_num', 'svm', 'decision_trees', 'neural_net']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

	writer.writeheader()

	Corpus = kindred.load(dataFormat='json',path='db/1')

	# avg_svm = 0
	# avg_dct = 0
	# avg_nn = 0

	count = 0
	iter_num = 400

	print("-------------5 CLASSES------------")

	while count < iter_num:
		print("------",count,"------")

		trainCorpus,devCorpus = Corpus.split(trainFraction=0.9)

		predictionCorpus = devCorpus.clone()
		predictionCorpus.removeRelations()

		classifier = kindred.RelationClassifier()
		classifier.train(trainCorpus)
		classifier.predict(predictionCorpus)
		svmf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
		print("svm:\t", svmf1score)
		# avg_svm = avg_svm+svmf1score

		classifier = kindred.RelationClassifier(classifierType='DCT')
		classifier.train(trainCorpus)
		classifier.predict(predictionCorpus)
		dctf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
		print("dct:\t", dctf1score)	
		# avg_dct = avg_dct+dctf1score

		classifier = kindred.RelationClassifier(classifierType='NN')
		classifier.train(trainCorpus)
		classifier.predict(predictionCorpus)
		nnf1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score',display=False)
		print("nn:\t", nnf1score)	
		# avg_nn = avg_nn+nnf1score

		writer.writerow({'iteration_num': count, 'svm': svmf1score, 'decision_trees': dctf1score, 'neural_net': nnf1score})

		count += 1
		
	# avg_svm = avg_svm/iter_num
	# avg_dct = avg_dct/iter_num
	# avg_nn = avg_nn/iter_num

	# print("average of SVM:", avg_svm)
	# print("average of DCT:", avg_dct)
	# print("average of Neural Networks:", avg_nn)


	# writer.writerow({'iteration_num': iter_num, 'svm': avg_svm, 'decision_trees': avg_dct, 'neural_net': avg_nn})