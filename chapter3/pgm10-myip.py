import urllib
import json
print "IP address:",json.load(urllib.urlopen('http://httpbin.org/get'))['origin']


