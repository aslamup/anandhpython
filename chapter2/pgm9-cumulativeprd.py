def cumulative_product(s):
	p=1
	l=[]
	for i in s:
		p=p*i
		l.append(p)
	return l
print cumulative_product([4,3,2,1])
