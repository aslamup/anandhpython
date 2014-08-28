def exsort(l):
	return sorted(l,key=lambda x :x[x.find('.'):])

print exsort(['x.js','a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
