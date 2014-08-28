import textwrap
def wrap(filename,width):
	f=open('foo.txt').readlines()
	for i in f:
		k=textwrap.wrap(i,width)
		for j in k:
			print j
			
		
wrap('foo.txt',30)
