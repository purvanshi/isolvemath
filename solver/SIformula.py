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
	return si

def find_time(p,r,si):
	print(p,r,si)
	t=(si*100)/(p*r)
	print("Time=")
	return t

def find_rate(p,t,si):
	if(t==0):
		t=1
	r=(si*100)/(p*t)
	print("rate is")
	return r

def find_amt(interest,principal):
	print("finding amount")
	amount=interest+principal
	print("amount is")
	return amount
