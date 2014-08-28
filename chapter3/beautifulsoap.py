from bs4 import BeautifulSoup
import urllib
html = urllib.urlopen("http://python.org/")
soup=BeautifulSoup(html)
print soup.findAll('a')
