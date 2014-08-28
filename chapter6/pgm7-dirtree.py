#Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.
#Hint: Use os.listdir and os.path.isdir funtions.

import sys
import os
dirname=sys.argv[1]
print os.path.basename(dirname)
a='|-- '
b='|  '
i=0
k='.'
def dirtree(dirname,i):
    filenames=os.listdir(dirname)
    for filename in filenames:
        if not os.path.isdir(os.path.abspath(dirname + '/' + filename)):
            if filename==filenames[-1]:
                print b*i+'\--',filename
            else:
                print b*i+ a,filename
        else:
            print b*i +'|-- ',filename
            dirname=dirname+'/'+filename
            dirtree(dirname,i+1)
dirtree(dirname,i)
