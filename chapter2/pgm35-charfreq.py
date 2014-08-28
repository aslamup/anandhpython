import string
def character_frequency(filename):
	f=open(filename).read()
	a=f.lower()
	for i in range(len(f)):
		if a[i] =="\n" or a[i] ==" " or (a[i] in string.punctuation):
			i += 1
		elif a[i] in a[:i]:
			i += 1
		else:
			 print "Count of %s is %d" %(a[i],a.count(a[i]))
print character_frequency('foo.txt')
