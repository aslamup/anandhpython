# function to compute the number of python files (.py extension) in a specified directory recursively.
import sys
import os
l=[]
def extension_count(dirname):
    filenames=os.listdir(dirname)
    for filename in filenames:
        x=filename.split(".")
        l.append(x[1])
    print "\nThe number of python files is",l.count('py'),"\n"
extension_count(sys.argv[1])
