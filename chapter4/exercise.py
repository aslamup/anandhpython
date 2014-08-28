# What will the output of the following program.???

class Aslam:
    def f(self):
        return self.g()

    def g(self):
        return 'Aslam'

class Baby(Aslam):
    def g(self):
        return 'Baby'

a = Aslam()
b = Baby()
print a.f(), b.f()
print a.g(), b.g()
