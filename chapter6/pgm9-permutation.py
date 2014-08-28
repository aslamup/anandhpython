import itertools
def permute(l):
    return itertools.permutations(l)
x=permute([1,2,3])
print list(x)
