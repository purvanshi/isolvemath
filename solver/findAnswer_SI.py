import common_functions
import SIformula

def oneMoney(dep,doc,pattern,unknown,rate,time):
	interest=0
	principal=0
	amount=0
	ratios=[]
	for triple in dep.triples():
		q_dep=[]
		for ent in doc.ents:
			if(ent.label_=="MONEY"):
				pq=common_functions.clean(ent.text)
				com=common_functions.clean(triple[0][0])
				com1=common_functions.clean(triple[2][0])
				if(com==pq or com1==pq):
					money=pq
					q_dep.append(triple)
	q_dep = str(q_dep)

	#Matching with the closest pattern and classifying money as SI, principal or amount
	for i in range(len(pattern)):
		m=common_functions.SequenceMatcher(None,pattern["pattern"][i],q_dep)
		q=m.ratio()
		ratios.append(q)

	mx=max(ratios)
	ino=ratios.index(mx)
	answer=pattern["tag"][ino]
	print("printing tagged")
	print(answer,money)
	if(answer=="p" and (unknown==3 or unknown==5)):
		principal=money
		principal=common_functions.isfloat(principal)

	elif(answer=="si" and unknown==2 or unknown==5):
		interest=money
		interest=common_functions.isfloat(interest)

	elif(answer=="p" and unknown==2):
		interest=money
		interest=common_functions.isfloat(interest)

	elif(answer=="si" and unknown==3):
		principal=money
		principal=common_functions.isfloat(principal)

	elif(unknown==4 and answer=="si"):
		interest=money
		interest=common_functions.isfloat(interest)
		unknown=2

	elif(unknown==4 and answer=="p"):
		principal=money
		principal=common_functions.isfloat(principal)
		unknown=3

	if(unknown==2):
		print("principal=")

		answer=SIformula.find_principal(rate,interest,time)
		print(answer)
	elif(unknown==3):
		answer=SIformula.find_si(principal,rate,time)
		print(answer)
	elif(unknown==5):
		if(principal==0):
			print("principal=")
			prin=SIformula.find_principal(rate,interest,time)
			answer=SIformula.find_amt(interest,prin)
			print(answer)
		elif(interest==0):
			interest=SIformula.find_si(principal,rate,time)
			answer=SIformula.find_amt(interest,principal)
			print(answer)
	return answer

def moreMoney(dep,doc,pattern,unknown,rate,time):
	q_dep=[]
	interest=0
	principal=0
	amount=0
	ratios=[]
	for ent in doc.ents:
		if(ent.label_=="MONEY"):
			print(principal,interest,amount)
			q_dep=[]
			for triple in dep.triples():
				pq=common_functions.clean(ent.text)
				com=common_functions.clean(triple[0][0])
				com1=common_functions.clean(triple[2][0])
				if(com==pq or com1==pq):
					money=pq
					q_dep.append(triple)
			q_dep = str(q_dep)
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
				amount=common_functions.isfloat(amount)
			
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
				interest=common_functions.isfloat(interest)
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
					principal=common_functions.isfloat(principal)
				elif(answer=="a"):
					amount=money
					amount=common_functions.isfloat(amount)

			elif(answer=="p" and unknown!=2 and principal==0):
				principal=money
				principal=common_functions.isfloat(principal)

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
					interest=common_functions.isfloat(interest)
				elif(answer=="a"):
					q=common_functions.re.search(r'interest of \d+',question)
					w=common_functions.re.search(r'\d+ as interest',question)
					if(q or w and interest==0):
						interest=money
						interest=common_functions.isfloat(interest)
					else:
						amount=money
						amount=common_functions.isfloat(amount)

	print(principal,interest,amount)
	if(interest!=0 and principal!=0 and unknown==5):
		amount=principal+interest
		print(amount)
	elif(unknown==0):
		if(interest!=0 and principal!=0):
			answer=SIformula.find_time(principal,rate,interest)
			print(answer)
		elif(amount!=0 and principal!=0):
			interest=amount-principal
			answer=SIformula.find_time(principal,rate,interest)
			print(answer)
		elif(amount!=0 and interest!=0):
			principal=amount-interest
			answer=SIformula.find_time(principal,rate,interest)
			print(answer)
	elif(unknown==1):
		if(interest!=0 and principal!=0):
			answer=SIformula.find_rate(principal,time,interest)
			print(answer)
		elif(amount!=0 and principal!=0):
			interest=amount-principal
			answer=SIformula.find_rate(principal,time,interest)
			print(answer)
		elif(amount!=0 and interest!=0):
			principal=amount-interest
			answer=SIformula.find_rate(principal,time,interest)
			print(answer)
	if 'answer' not in locals():
		answer = "No small talk just ask, a simple interest question." # nope
	return answer