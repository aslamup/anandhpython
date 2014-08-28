def valuesort(d):
	l=[]
	for key in d:
		l.append(key)
	s=[]
	for i in sorted(l):
		s.append(d[i])
	return s
print valuesort({'x':1, 'y':2,'a':3,})
