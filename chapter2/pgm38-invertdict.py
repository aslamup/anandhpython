def invertdict(d):
	for key,value in d.items():
		del d[key]
		d.setdefault(value,key)
	return d
print invertdict({'x':1,'y':2,'z':3})
