class BankAccount:
	def __init__(self):
		self.balance=0
	def deposit(self,amount):
		self.balance += amount
	def withdraw(self,amount):
			self.balance -= amount
			print self.balance
	def showbalance(self):
		return self.balance
class MinimumBalanceAccount(BankAccount):
	def __init__(self, minimum_balance):
		BankAccount.__init__(self)
		self.minimum_balance = minimum_balance
	def withdraw(self,amount):
		if self.balance - amount < self.minimum_balance:
			print "Sorry, minimum balance must be maintained."
		else:
			BankAccount.withdraw(self,amount)

a=MinimumBalanceAccount(100)
a.deposit(500)
a.withdraw(450)
