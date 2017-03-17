import numpy as np
import pandas as pd
from sklearn import datasets,preprocessing,linear_model
import nltk
from nltk.classify import ClassifierI
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser
from nltk.internals import find_jars_within_path
import csv 
import sys
import re
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup   
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def read(name):
	train = pd.read_csv(name, header=0)
	return train


def cleandata(name):
	letter=[]
	word=[]
	for i in range(len(name)):
		letters_only = re.sub("[^a-zA-Z]", " ", name[i][0])
		words = name[i][0].lower().split()
		letter.append(letters_only)
		word.append(words)
	stops = set(stopwords.words("english")) 
	meaningful_words = [w for w in words if not w in stops]   
	return( " ".join( meaningful_words ))  

def bag_of_words(name):
	vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,\
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 
	vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', 
           stop_words=None)
	a=vect.fit_transform(name)
	#corpus_tf_idf = vect.transform(name) 
	#train_data_features = vectorizer.fit_transform(name[i])
	#train_data_features= map(vectorizer.fit_transform,name)
	#train_data_features = train_data_features.toarray()
	#train_data_features=np.fromiter(train_data_features, dtype=np.int)
	#print(train_data_features)
	print("hey")
	return(a)

def letters_only(name):	
	final=[]
	for i in range(len(name["questions"])):
		letters_only = re.sub("[^a-zA-Z]", " ", name["questions"][i])
		final.append(letters_only)
	return final




percentage=read("Percentage.csv")
unitary=read("unitary.csv")
dst=read("dst.csv")
profit=read("profit.csv")

stop_words = set(stopwords.words("english"))
l_unitary=letters_only(unitary)
l_dst=letters_only(dst)

final=[]
for i in range(len(l_unitary)):
   	for sent in sent_tokenize(l_unitary[i]):
	    words = word_tokenize(sent)
	    filtered_sentence = [w for w in words if not w in stop_words]
	    final.append(filtered_sentence)
unit=final
print("done after unitary cleaning")
print(final)

final=[]

for i in range(len(l_dst)):
   	for sent in sent_tokenize(l_dst[i]):
	    words = word_tokenize(sent)
	    filtered_sentence = [w for w in words if not w in stop_words]
	    final.append(filtered_sentence)

ds=final
print(final)
values = ','.join(str(v) for v in final)
print(values)
print("after dst cleaning")

feature_ds=bag_of_words(ds)
feature_unit=bag_of_words(unit)

print(feature_ds.shape)
print(feature_unit)

