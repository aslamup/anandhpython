def grep(filename,word):
	f=open(filename).readlines()
	for line in f:
		if word in line:
			print line
grep('foo.txt','sure')
	
