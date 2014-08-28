def integers():
	"""Infinite sequence of integers."""
	i=1
	while True:
		yield i
		i=i+1
def square():
	for i in integers():
		yield i*i
def cube():
	for i in integers():
		yield i*i*i
pyt=((x,y,z) for z in integers() for y in xrange(1,z) for x in range(1,y) if x*x + y*y ==z*z)
def take(n,seq):
	"""Returns first n values from the given sequence."""
	seq = iter(seq)
	result=[]
	try:
		for i in range(n):
			result.append(seq.next())
	except StopIteration:
		pass
	return result

print take(5,pyt)
