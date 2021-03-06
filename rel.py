import kindred
import argparse
import os

trainCorpus = kindred.load(dataFormat='json',path='relation/db/1')
devCorpus = kindred.load(dataFormat='json',path='ner-dump')

predictionCorpus = devCorpus.clone()

classifier = kindred.RelationClassifier()
classifier.train(trainCorpus)
classifier.predict(predictionCorpus)

f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score')

for i in predictionCorpus.getRelations():
  print(i)
