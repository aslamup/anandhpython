def cumulative_sum(s):
	sum=0
	l=[]
	for i in s:
		sum=sum+i
		l.append(sum)
	return l
print cumulative_sum([1,2,3,4])
		
