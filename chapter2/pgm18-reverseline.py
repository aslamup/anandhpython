import sys
def reverse(filename):
	f=open(filename).readlines()
	for i in f:
		print i[::-1]
reverse(sys.argv[1])
