def dups(s):
	l=[]
	for i in range(len(s)):
		if s.count(s[i]) != 1:
			l.append(s[i])
	return list(set(l))
print dups([3,8,7,1,5,3,3,1,2,1,2])
