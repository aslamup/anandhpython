# This is a program to find the sum of elements in a list:
def sum(s):
	sum=0
	for i in s:
		sum=sum+i
	return sum
n=input("Enter the length of list:")
s=[]
for j in range(n):
	n1=input("Enter the list elements:")
	s.append(n1)
print "list",s
print "sum of list", sum(s)
