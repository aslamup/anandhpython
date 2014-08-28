def zip(a,b):
	return [(a[x],b[y]) for x in range(len(a)) for y in range(x,x+1)]
print zip(['1','2','3'],['a','b','c'])
