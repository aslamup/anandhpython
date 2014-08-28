# To model a bank account with support for deposit and withdraw operations..

balance=0
x=input("enter the amount deposited")
def deposit(amount):
	global balance
	balance += amount
	return balance
y=input("enter the amount to withdraw")
def withdraw(amount):
	global balance
	balance -=amount
	return balance
deposit(x)
print "Your final balance after withdrawal is",withdraw(y)
