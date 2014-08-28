def unique(x):
	y=[]
	for i in x:
		if i.lower() not in y:
			y.append(i)
	return y
print unique(["python", "java", "Python", "Java"])

