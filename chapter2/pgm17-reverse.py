import sys
def reverse(filename):
	f=open(filename).readlines()
	for lines in f[::-1]:
		print lines
reverse(sys.argv[1])
