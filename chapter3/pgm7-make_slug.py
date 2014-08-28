import re
def make_slug():
	a=re.findall(r'\w+',s)
	print '-'.join(a)
s=raw_input('Enter the string:\n')
make_slug()
