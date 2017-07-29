import numpy as np
import pandas as pd
import nltk
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
from sklearn import svm
from sklearn import preprocessing
from difflib import SequenceMatcher
import re


jar = 'libs/stanford-postagger-full/stanford-postagger.jar'
model = 'libs/stanford-postagger-full/models/english-left3words-distsim.tagger'
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

path_to_jar = 'libs/stanford-parser-full/stanford-parser.jar'
path_to_models_jar = 'libs/stanford-parser-full/stanford-parser-3.8.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
nlp = spacy.load('en')


def clean(text):
	money = text.replace(',', '')
	rate=re.findall(r"[-+]?\d*\.\d+|\d+", money)
	if rate==[]:
		return 0
	else:
		return rate[0]

def traindata():
	training=[]
	nlp = spacy.load('en')
	for i in range(len(si)):
		doc = nlp(si["Question"][i])
		result = dependency_parser.raw_parse(si["Question"][i])
		dep = result.__next__()
		cool=list(dep.triples())
		for triple in dep.triples():
		    for ent in doc.ents:
		    	if(triple[0][0]==ent.text or triple[2][0]==ent.text and ent.label_=="MONEY"):
		    		print(triple[1],"(",triple[0][0],", ",triple[2][0],")")
		    		training.append(triple)
	
	for i in training:
		print(i)
	w, h = len(si)*2,2;
	Matrix = [[0 for x in range(w)] for y in range(h)] 
	print(len(Matrix))
	for i in range(len(si)):
		p=-1
		doc = nlp(si["Question"][i])
		for ent in doc.ents:
			if(ent.label_=="MONEY"):
				p=p+i
				Matrix[p][0]=ent.text
				Matrix[p][1]=si["tags"][i]
	print(Matrix)


def read(name):
	train = pd.read_csv(name, header=0)
	return train

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        p=int(x)
        l=float(p)
        return l
    else:
    	return a
  