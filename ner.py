import spacy
import json
import kindred
import argparse
import os
import sqlite3
from model import Relationships

# Scispacy

nlp1 = spacy.load('en_ner_bionlp13cg_md')

lines = [line.rstrip('\n') for line in open('ner-input.txt','r')]

fcounter = 1
for i in range(0, len(lines)):
  if lines[i] == "TEST":
    # print("TEST --------------------------------------")
    docx1 = nlp1(lines[i+1])
    entities = []
    count = 1
    gene_list = []
    disease_list = []
    for token in docx1.ents:
      if token.label_ == "GENE_OR_GENE_PRODUCT":
        obj = "gene"
        if token.text not in gene_list:
          gene_list.append(token.text)
          dict1 = {"id": "T{}".format(count), "obj": obj, "span": {"begin": token.start_char, "end": token.end_char}}
          entities.append(dict1)
          count = count + 1
          # print(token.text, token.start_char, token.end_char, token.label_)
      elif (token.label_ == "CANCER"):
        obj = "disease"
        if token.text not in disease_list:
          disease_list.append(token.text)
          dict1 = {"id": "T{}".format(count), "obj": obj, "span": {"begin": token.start_char, "end": token.end_char}}
          entities.append(dict1)
          count = count + 1
          # print(token.text, token.start_char, token.end_char, token.label_)
      # print(token.text, token.start_char, token.end_char, token.label_)

    dict2 = {"text":lines[i+1], "denotations":entities}

    with open("ner-dump/{}.json".format(fcounter), "a") as f:
      print(json.dumps(dict2), file=f)
    fcounter = fcounter + 1


# DATABASE

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE relationships (
            gene text,
            disease text,
            relation text,
            text text
            )""")


def insert_rels(rel):
  with conn:
    c.execute("INSERT INTO relationships VALUES (:gene, :disease, :relation, :text)", {'gene': rel.gene, 'disease': rel.disease, 'relation': rel.relation, 'text': rel.text})


def get_rels():
  c.execute("SELECT * FROM relationships")
  return c.fetchall()

def get_rels_clean():
  c.execute("SELECT gene, disease, relation FROM relationships")
  return c.fetchall()

# Kindred

# 5 classes

trainCorpus = kindred.load(dataFormat='json',path='relation/db/1')
devCorpus = kindred.load(dataFormat='json',path='ner-dump')

predictionCorpus = devCorpus.clone()

classifier = kindred.RelationClassifier()
classifier.train(trainCorpus)
classifier.predict(predictionCorpus)

f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score')

print("5 CLASSES ---------------------")
for i in predictionCorpus.documents:
  for j in (i.relations):
    rel = Relationships(j.entities[0].text, j.entities[1].text, j.relationType, i.text)
    insert_rels(rel)


result = get_rels()
for i in result:
  print(i)

result = get_rels_clean()
for i in result:
  print(i)

conn.close()

# 3 classes

# trainCorpus = kindred.load(dataFormat='json',path='relation/db/4')
# devCorpus = kindred.load(dataFormat='json',path='ner-dump')

# predictionCorpus = devCorpus.clone()

# classifier = kindred.RelationClassifier()
# classifier.train(trainCorpus)
# classifier.predict(predictionCorpus)

# f1score = kindred.evaluate(devCorpus, predictionCorpus, metric='f1score')

# print("3 CLASSES ---------------------")
# for i in predictionCorpus.getRelations():
#   print(i)