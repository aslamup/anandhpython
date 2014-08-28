def parse_csv(filename):
	print open(filename).read()
	f=open(filename)
	l=[]
	for i in f.readlines():
		l.append([i])
	return l
	f.close()
	

print parse_csv('a.csv')
