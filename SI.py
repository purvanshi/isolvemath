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
import editdistance
import re

def read(name):
	train = pd.read_csv(name, header=0)
	return train

def adv_final(question,nerquestion,posquestion,qdep):
	print("Advance searching")
	print(qdep)
	print(qdep[0][1])

def find(question,name):
	sen_list=sent_tokenize(name)
	no_sen=nltk.FreqDist(sent_tokenize(name)).N()
	final=[]
	j=0
	print(no_sen)
	if(no_sen==1):
		j=0
		fin=0
		for i in question:
			if(fin==0):
				j=j+1
				if(i[1]=="WDT" or i[1]=="WRB" or i[0]=="find" or i[0]=="Find" or i[0]=="FIND" or i[0]=="Calculate" or i[0]=="calculate" ):
					fin=1
					print("n")
					while(i[1]!="MD" or i[0]=="." or i[0]=="?"):
						if (i[0]=="." or i[0]=="?"):
							break
						print(i[0])
						final.append(i[0])
						i=question[j]
						j=j+1
	else:
		j=0
		print(question)
		fin=0
		for i in question:
			if(fin==0):
				j=j+1
				if(i[1]=="WDT" or i[1]=="WRB" or i[1]=="WP"or i[0]=="find" or i[0]=="Find" or i[0]=="Calculate" or i[0]=="calculate"):
					fin=1
					while(i[1]!="." or i[1]!="?"):
						print(i[0])
						if (i[0]=="." or i[0]=="?"):
							break
						final.append(i[0])
						i=question[j]
						j=j+1

	p=0
	print(final)
	#q=re.search(r'interest rate',final)
	#w=re.search(r'rate of interest',final)
	#if(q):
	#	p=1
	#	return 3
	#if(w):
	#	p=1
	#	return 
	for i in final:
		if(i=="time" and p==0):
			print("time")
			p=1
			return 0
	for i in final:
		if(i=="rate" and p==0):
			print("rate")
			p=1
			return 1
	for i in final:
		if(i=="principal" and p==0):
			print("principal")
			p=1
			return 2
	for i in final:
		if(i=="interest" and p==0):
			print("int")
			p=1
			return 3
	for i in final:
		if(i=="amount" or i=="total" and p==0):
			print("amount")
			p=1
			return 5
	if(p==0):
		return 4

def find_principal(rate,interest,time):
	float(interest)
	float(rate)
	if(time==0):
		time=1
	float(time)
	print(rate,interest,time)
	p=(interest*100)
	q=(rate*time)
	q=float(q)
	n=p/q
	print("principal=")
	print(n)
	return n

def find_si(p,r,t):
	p=float(p)
	r=float(r)
	if(t==0):
		t=1
	t=float(t)
	si=p*r*t
	si=si/100
	print("Simple interest=")
	print(si)
	return si

def find_time(p,r,si):
	print(p,r,si)
	t=(si*100)/(p*r)
	print("Time=")
	print(t)
	return t

def find_rate(p,t,si):
	if(t==0):
		t=1
	r=(si*100)/(p*t)
	print("rate is")
	print(r)
	return r

def find_amt(interest,principal):
	print("finding amount")
	amount=interest+principal
	print(amount)
	return amount

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


def numchange(pattern):
	print(pattern)
	for i in range(len(pattern)):
		print(pattern.triples())
		if(pattern[i][0][1]=='CD' ):
			pattern[i][0][0]=="NUMBER"
		elif(pattern[2][1]=='CD'):
			pattern[2][0]=="NUMBER"
	print(pattern)
	return(pattern)

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        p=int(x)
        l=float(p)
        return l
    else:
    	return a
        
def clean(text):
	money = text.replace(',', '')
	rate=re.findall(r"[-+]?\d*\.\d+|\d+", money)
	if rate==[]:
		return 0
	else:
		return rate[0]



jar = '/home/puru/Documents/d/arithmetic/code/stanford-postagger-2016-10-31/stanford-postagger.jar'
model = '/home/puru/Documents/d/arithmetic/code/stanford-postagger-2016-10-31/models/english-left3words-distsim.tagger'
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')

path_to_jar = '/home/puru/Documents/d/arithmetic/code/stanford-parser-full-2015-12-09/stanford-parser.jar'
path_to_models_jar = '/home/puru/Documents/d/arithmetic/code/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
print("enter question")
question=input()
#text=st.tag(question.split())
#print(text)
nlp = spacy.load('en')
text=pos_tagger.tag(nltk.word_tokenize(question))
doc = nlp(question)
unknown=find(text,question)
print(unknown)
time=0
rate=0
for ent in doc.ents:
    print(ent.label_, ent.text)
    if(ent.label_=="PERCENT" and rate==0):
    	frate=ent.text
    	rate=clean(frate)
    	print(rate)
    	rate=isfloat(rate) 		
    elif(ent.label_=="DATE"  and time==0):
    	t=ent.text
    	time=clean(t)
    	time=isfloat(time)

pattern=read("pattern.csv")

p=0
for ent in doc.ents:
	if(ent.label_=="MONEY"):
		p=p+1

loops=p

doc = nlp(question)
result = dependency_parser.raw_parse(question)
dep = result.__next__()
q_dep=[]
interest=0
principal=0
amount=0
if (p==1):
	for triple in dep.triples():
		for ent in doc.ents:
			if(ent.label_=="MONEY"):
				pq=clean(ent.text)
				com=clean(triple[0][0])
				com1=clean(triple[2][0])
				if(com==pq or com1==pq):
					money=pq
					q_dep.append(triple)	
	q_dep = str(q_dep)
	ratios=[]
	print("to find")
	print(unknown)
	for i in range(len(pattern)):
		m=SequenceMatcher(None,pattern["pattern"][i],q_dep)
		q=m.ratio()
		ratios.append(q)
	mx=max(ratios)
	ino=ratios.index(mx)
	answer=pattern["tag"][ino]
	print("printing tagged")
	print(answer,money)
	if(answer=="p" and (unknown==3 or unknown==5)):
		principal=money
		principal=isfloat(principal)
	
	elif(answer=="si" and unknown==2 or unknown==5):
		interest=money
		interest=isfloat(interest)	

	elif(answer=="p" and unknown==2):
		interest=money
		interest=isfloat(interest)

	elif(answer=="si" and unknown==3):
		principal=money
		principal=isfloat(principal)

	elif(unknown==4 and answer=="si"):
		interest=money
		interest=isfloat(interest)
		unknown=2

	elif(unknown==4 and answer=="p"):
		principal=money
		principal=isfloat(principal)
		unknown=3

	if(unknown==2):
		find_principal(rate,interest,time)
	elif(unknown==3):
		find_si(principal,rate,time)
	elif(unknown==5):
		if(principal==0):
			prin=find_principal(rate,interest,time)
			find_amt(interest,prin)
		elif(interest==0):
			interest=find_si(principal,rate,time)
			find_amt(interest,principal)

elif(p>1):
	for ent in doc.ents:
		if(ent.label_=="MONEY"):
			print(principal,interest,amount)
			q_dep=[]
			for triple in dep.triples():
				pq=clean(ent.text)
				com=clean(triple[0][0])
				com1=clean(triple[2][0])
				if(com==pq or com1==pq and ent.label_=="MONEY"):
					money=pq
					q_dep.append(triple)
			q_dep = str(q_dep)	
			ratios=[]
			for i in range(len(pattern)):
				m=SequenceMatcher(None,pattern["pattern"][i],q_dep)
				q=m.ratio()
				ratios.append(q)
			mx=max(ratios)
			ino=ratios.index(mx)
			answer=pattern["tag"][ino]			
			print(answer,unknown)

			if(answer=="a" and unknown!=5 and amount==0):
				amount=money
				amount=isfloat(amount)
			
			elif(answer=="a" and unknown==5 or amount!=0):
				for i in range(len(pattern)):
					if(pattern["tag"][i]!="a"):
						m=SequenceMatcher(None,pattern["pattern"][i],q_dep)
						q=m.ratio()
						ratios.append(q)
						mx=max(ratios)
				ino=ratios.index(mx)
				answer=pattern["tag"][ino]

			elif(answer=="si" and unknown!=3 and interest==0):
				print("tagging int")
				interest=money
				interest=isfloat(interest)
				print(interest)

			elif(answer=="si" and unknown==3 or interest!=0):
				q=0
				maxo=0
				for i in range(len(pattern)):
					if(pattern["tag"][i]=="p" or pattern["tag"][i]=="a"):
						m=SequenceMatcher(None,pattern["pattern"][i],q_dep)
						q=m.ratio()
						if(q>=maxo):
							maxo=q
							maxoindex=i
				answer=pattern["tag"][maxoindex]
				if(answer=="p"):
					principal=money
					principal=isfloat(principal)
				elif(answer=="a"):
					amount=money
					amount=isfloat(amount)

			elif(answer=="p" and unknown!=2 and principal==0):
				principal=money
				principal=isfloat(principal)

			elif(answer=="p" and (unknown==2 or principal!=0)):
				q=0
				maxo=0
				for i in range(len(pattern)):
					if(pattern["tag"][i]=="si" or pattern["tag"][i]=="a"):
						m=SequenceMatcher(None,pattern["pattern"][i],q_dep)
						q=m.ratio()
						if(q>=maxo):
							maxo=q
							maxoindex=i
				answer=pattern["tag"][maxoindex]
				print(answer)
				if(answer=="si"):
					interest=money
					interest=isfloat(interest)
				elif(answer=="a"):
					q=re.search(r'interest of \d+',question)
					w=re.search(r'\d+ as interest',question)
					if(q or w and interest==0):
						interest=money
						interest=isfloat(interest)
					else:	
						amount=money
						amount=isfloat(amount)

	print(principal,interest,amount)
	if(interest!=0 and principal!=0 and unknown==5):
		amount=principal+interest
		print(amount)
	elif(unknown==0):
		if(interest!=0 and principal!=0):
			find_time(principal,rate,interest)
		elif(amount!=0 and principal!=0):
			interest=amount-principal
			find_time(principal,rate,interest)
		elif(amount!=0 and interest!=0):
			principal=amount-interest
			find_time(principal,rate,interest)
	elif(unknown==1):
		if(interest!=0 and principal!=0):
			find_rate(principal,time,interest)
		elif(amount!=0 and principal!=0):
			interest=amount-principal
			find_rate(principal,time,interest)
		elif(amount!=0 and interest!=0):
			principal=amount-interest
			find_rate(principal,time,interest)


#le = preprocessing.LabelEncoder()
#for i in range(len(pattern)):
#    myData[:,i]= le.fit_transform(pattern["pattern"][:,i])
#clf = svm.SVC(kernel='linear', C = 0.6)
#clf.fit(pattern["pattern"],pattern["tag"])
#
#clf.predict(q_dep)
#print(doc.ents)
#ratios=[]
#print(q_dep)
#for i in range(len(pattern)):
#	a=editdistance.eval(pattern["pattern"][i], q_dep)
#	#print(pattern["pattern"][i],a)
#	print(a)
#	print(i)
#	ratios.append(a)

