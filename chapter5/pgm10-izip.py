#Implement a function izip that works like itertools.izip.
def izip(l1,l2):
    if len(l1)>len(l2):
        for i in range(len(l2)):
            a=l1[i]
            b=l2[i]
            yield a,b
    else:
        for j in range(len(l1)):
            a=l1[j]
            b=l2[j]
            yield a,b
a=izip(["a","b","c"],[1,2,3])
for x,y in list(a):
    print x,y
