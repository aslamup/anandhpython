import sys
print "~~~Head elements~~~"
def head(filename):
	f=open(filename)
	for i in range(5):
		print f.readline()
head(sys.argv[1])
print "~~~Tail elements ~~~"
def tail(filename):
	f=open(filename).readlines()
	s=f[::-1]
	l=[]
	for i in range(5):
		l.append(s[i])
	for j in l[::-1]:
		print j

tail(sys.argv[1])
