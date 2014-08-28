# Program to find factorial of a number
def product(l):
	p=1
	for i in l:
		p=p*i
	return p
def factorial(x):
	return product(range(1,x+1))
x=input("Enter the number:")
print 'factorial=',factorial(x)
