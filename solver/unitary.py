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

def read(name):
	train = pd.read_csv(name, header=0)
	return train


file=read("UnitaryMethod.csv")
print(file)

