import nltk.data
import os
import json
from collections import OrderedDict

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test_corpus.txt")
wf = open("answer.json", "w")
data = fp.read()
# print '\n-----\n'.join(tokenizer.tokenize(data))
sentences = tokenizer.tokenize(data)
done = ""

for i in sentences:
	m_dict = json.loads('{"text": "'+str(i)+'", "denotations": []}', object_pairs_hook=OrderedDict)

	print(sentences.index(i)+1)
	print(i)
	
	d_arr = []
	word = raw_input('word: ')
	while word!="x":
		first = i.find(word)
		last = int(first)+len(word)

		d_dict = json.loads('{"id": "T1", "obj": "'+word+'","span":{"begin": '+str(first)+',"end":'+str(last)+'}'+'}', object_pairs_hook=OrderedDict)
		d_arr.append(d_dict)

		print('First:', first)
		print('Last:', last)

		word = raw_input('word: ')
	word = ""

	m_dict["denotations"] = d_arr
	# print(json.dumps(m_dict, indent = 4))
	wf.write(json.dumps(m_dict, indent = 4))
	
	os.system('clear')

fp.close()