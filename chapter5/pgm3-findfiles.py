#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.
import os
import sys
def findfiles(dirname):
    for root,dirs,filenames in os.walk(dirname):
        for filename in filenames:
           yield os.path.join(root,filename)
paths=findfiles(sys.argv[1])
for path in paths:
    print path
