import urllib
import os
import sys
url =sys.argv[1]
if url[-1]=='/':
	basename='index.html'
else:
	basename=url.split('/')[-1]
print 'saving ',url,' as',basename
urllib.urlretrieve(url,os.getcwd()+'/'+basename)
