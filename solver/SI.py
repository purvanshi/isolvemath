import common_functions
import findAnswer_SI

def find(question,name):
	sen_list=common_functions.sent_tokenize(name)
	no_sen=common_functions.nltk.FreqDist(common_functions.sent_tokenize(name)).N()
	final=[]
	j=0
	print(name)
	print(no_sen)
	if(no_sen==1):
		j=0
		fin=0
		for i in question:
			if(fin==0):
				j=j+1
				if(i[1]=="WDT" or i[1]=="WRB" or i[0]=="find" or i[1]=="WP" or i[0]=="Find" or i[0]=="FIND" or i[0]=="Calculate" or i[0]=="calculate" ):
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

def main(input_question):
	pattern=common_functions.read("Data/pattern.csv")
	question=input_question
	tagged_question=common_functions.pos_tagger.tag(common_functions.nltk.word_tokenize(question))
	result = common_functions.dependency_parser.raw_parse(question)
	doc = common_functions.nlp(question)
	print(tagged_question)
	unknown=find(tagged_question,question)
	time=0
	rate=0

	#Find the rate of percentage and time given in the question
	for ent in doc.ents:
	    print(ent.label_, ent.text)
	    if(ent.label_=="PERCENT" and rate==0):
	    	frate=ent.text
	    	rate=common_functions.clean(frate)
	    	print(rate)
	    	rate=common_functions.isfloat(rate) 		
	    elif(ent.label_=="DATE"  and time==0):
	    	t=ent.text
	    	time=common_functions.clean(t)
	    	time=common_functions.isfloat(time)

	#Find number of amounts given in the question
	p=0
	for ent in doc.ents:
		if(ent.label_=="MONEY"):
			p=p+1
	loops=p
	dependency = result.__next__()
	if (p==1):
		findAnswer_SI.oneMoney(dependency,doc,pattern,unknown,rate,time)
		
	elif(p>1):
		findAnswer_SI.moreMoney(dependency,doc,pattern,unknown,rate,time)
		
print("enter question")
a=input()
main(a)