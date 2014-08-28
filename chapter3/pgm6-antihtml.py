import re
import sys
import urllib
import os
url=sys.argv[1]
if url[-1]=='/':
	basename='index.html'
else:
	basename=url.split('/')[-1]
print 'saving',url,' as', basename 
urllib.urlretrieve(url,os.getcwd()+'/'+basename)
f=open(basename,'r')
strings = re.findall(r'>[^<]+<', f.read())
for i in strings:
	print i[1:-1]
