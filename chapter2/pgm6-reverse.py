# To find the reverse of a list:
def rev(x):
	reverse=[]
	for i in range(len(x)-1,-1,-1):
		reverse.append(x[i])
	return reverse
print "\n~~Please enter a list of integers~~"
n=input("Enter the length of list:")
l=[]
for i in range(n):
	n1=input("Enter the element %d:" %i)
	l.append(n1)
print 'Original list',l
print 'Reversed list',rev(l)
