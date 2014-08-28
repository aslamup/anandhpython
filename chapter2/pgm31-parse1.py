def parse(filename,symbol,indicator):
	l=[]
	f=open(filename).readlines()
	for i in f:
		if i[0]!= '#':
			a=i.split("!")
			l.append(a)
	return l
print parse('a.txt','!','#')
