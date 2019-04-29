# Load Packages
from __future__ import unicode_literals, print_function

import plac #  wrapper over argparse
import random
from pathlib import Path
import spacy
from tqdm import tqdm # loading bar

nlp1 = spacy.load('en_core_sci_sm')

lines = [line.rstrip('\n') for line in open('input.txt','r')]


for i in range(0, len(lines)):
	if lines[i] == "TEST":
		print("TEST --------------------------------------")
		docx1 = nlp1(lines[i+1])
		for token in docx1.ents:
			print(token.text, token.start_char, token.end_char, token.label_)