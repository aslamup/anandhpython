import sys
import os
def extcount(filename):
        a=os.listdir(filename)
        l=[]
        for i in a:
                x=i.split('.')
                l.append(x[1])
        for j in range(len(l)):
                if l[j] in l[:j]:
                        j=j+1
                else:
                        print "Count of %s is %d" %(l[j],l.count(l[j]))
extcount(sys.argv[1])
