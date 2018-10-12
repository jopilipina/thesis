import os
import glob
import re

def main(text,g):
	a=re.compile(".*abstract.*", re.IGNORECASE)
	b=re.compile(".*background.*", re.IGNORECASE)
	c=re.compile(".*summary.*", re.IGNORECASE)
	for i in range(0,len(text)):
		if a.match(text[i]) or b.match(text[i]) or c.match(text[i]):
			count=0
			for j in range(i,len(text)):
				g.write(text[j])
				if text[j]=='':
					count+=1
				if count==2:
					return

for file in sorted(glob.glob('articles/*.pdf')):
	command='pdf2txt.py -o temp.txt '+file

	os.system(command)

	f=open('temp.txt')
	g=open('output.txt','a')

	g.write(file.strip('articles/'))
	g.write('\n')

	text = [line.strip('\n') for line in f]
	
	main(text,g)

	g.write('\n')
	g.write('\n')

	f.close()
	g.close()