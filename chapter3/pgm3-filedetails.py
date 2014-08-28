import sys
import os
dir=sys.argv[1]
filenames=os.listdir(os.path.abspath(dir))
print "filename \t size\t modification time"
for filename in filenames:
	print filename,'\t',os.stat(os.path.abspath(dir +'/'+ filename))[6],'\t',os.stat(os.path.abspath(dir +'/'+filename))[8]
