def enumerate(l):
	return [(x,l[y]) for x in range(len(l)) for y in range(x,x+1)]
print enumerate(["a","b","c"])
