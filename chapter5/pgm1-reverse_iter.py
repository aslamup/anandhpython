#Write an iterator class reverse_iter,that takes a list and iterates it fromthe reverse direction.

class reverse_iter():
	def __init__(self, l):
		self.data = l
		self.index = len(self.data)
	def __iter__(self):
		return self
	def next(self):
	        if self.index == 0:
		        raise StopIteration
	        else:
			self.index = self.index - 1
 			return self.data[self.index]

it = reverse_iter([1,2,3,4])
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
