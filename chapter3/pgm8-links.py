import re
import urllib
import sys
url = sys.argv[1]
f = urllib.urlopen(url)
text=re.findall(r'http://[\S\s]+"',f.read())
for i in text:
	print i[:-1]
