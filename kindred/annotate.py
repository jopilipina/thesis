import nltk.data
import os
import json

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test_corpus.txt")
wf = open("answer.json", "w")
data = fp.read()
# print '\n-----\n'.join(tokenizer.tokenize(data))
sentences = tokenizer.tokenize(data)
done = ""
for i in sentences:
	print(sentences.index(i)+1)
	print(i) # print sentence on terminal
	wf.write('{\n') 			
	datastore = '\t"text: "'+str(i)+'",\n'
	json.dumps(datastore, wf)												# {									# "text": "sentence",
	wf.write('\t"denotations":\n') 												# "denotations":
	word = raw_input('word: ')
	while word!="x":
		wf.write('\t\t[{"id":"T1", "obj":"'+word+'",\n')							# [{"id":"T1", "obj":"disease",
		first = i.find(word)
		last = int(first)+len(word)
		wf.write('\t\t"span":{"begin":'+str(first)+',"end":'+str(last)+'}},\n')		# "span":{"begin":4,"end":21}},
		print('First:', first)
		print('Last:', last)
		word = raw_input('word: ')
	word = ""
	wf.write('\t"relations"\n')													# "relations"
	wf.write('}\n') 															# }
	os.system('clear')
fp.close()
wf.close()
# text = ""
# text.find("word")
# len(word)
