# Program to find product of numbers in a list:
def product(x):
	s=1
	for i in x:
		s = s * i
	return s
print product([1,2,3,3,4])
