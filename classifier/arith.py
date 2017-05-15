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
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import svm

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
                             stop_words = None,  \
                             max_features = 10	) 
	train_data_features= map(vectorizer.fit_transform,name)
	return(train_data_features)

def letters_only(name):	
	final=[]
	for i in range(len(name["questions"])):
		letters_only = re.sub("[^a-zA-Z]", " ", name["questions"][i])
		final.append(letters_only)
	return final

def check_percentage(name):
	if "%" in name:
		return 1		
	elif "percentage" in name:
		return 1
	else:
		return 0

def hey(name):
	vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,\
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 
	vocab = vectorizer.get_feature_names()
	dist = np.sum(name, axis=0)
	for tag, count in zip(vocab, dist):
		print(tag)
		print(count)

#def insert(name):
#	l,h=name.shape
#	for i in range(len(name)):
#		name["Equations"][i]="n"
#		for key,value in globals().iteritems():
#	     	if type(value)==list and value==["questions","Equations"]:
#	     		print(key)
#	     	print("o")
#	    print("ak")
#	return name

a=input("enter question")
r=check_percentage(a)
if(r==1):
	print("classified as percentage")
percentage=read("Percentage.csv")
unitary=read("unitary.csv")
dst=read("dst.csv")
profit=read("profit.csv")
#percentage_final=insert(percentage)
#l,h=percentage.shape
#print(percentage[1][1])
#l,h=percentage.shape
#for i in range(len(percentage)):
#	percentage["Equations"][i]="percentage"
#
#l,h=dst.shape
#for i in range(len(dst)):
#	dst["Equations"][i]="dst"
#
#l,h=profit.shape
#for i in range(len(profit)):
#	profit["Equations"][i]="profit"
#
#l,h=unitary.shape
#for i in range(len(unitary)):
#	unitary["Equations"][i]="unitary"
#
traininglist=[]
	    
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

final=[]

for i in range(len(l_dst)):
   	for sent in sent_tokenize(l_dst[i]):
	    words = word_tokenize(sent)
	    filtered_sentence = [w for w in words if not w in stop_words]
	    final.append(filtered_sentence)

ds=final
values = ','.join(str(v) for v in final)
print("after dst cleaning")

feature_ds=np.array(list(bag_of_words(ds)))
feature_unit=np.array(list(bag_of_words(unit)))
c=np.concatenate((feature_ds,feature_unit))
print (list(bag_of_words(ds)))
a = np.zeros(shape=(200,2))
p=[]
for i in range(len(feature_ds)):
	p.append("ds")
	j=i+1

for i in range(len(feature_unit)):
	p.append("unit")
print(c.shape)
print(p.shape)
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(c,p)

#forest = RandomForestClassifier(n_estimators = 100) 
#forest = forest.fit(c,p)
