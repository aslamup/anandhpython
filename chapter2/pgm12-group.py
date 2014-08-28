def group(l,size):
	y=len(l)/size
	a=0
	b=size
	c=[]
	if len(l) % size==0:
		for i in range(y):
			c.append(l[a:b])
			a,b=b,b+size
		return c
	else:
		for j in range(y+1):
			c.append(l[a:b])
			a,b=b,b+size
		return c
print group([1,2,3,4,5,6,7,8,9],3)
print group([1,2,3,4,5,6,7,8,9],4)
