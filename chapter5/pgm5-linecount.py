#Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import sys
import os
def line_count(dirname):
    filenames=os.listdir(dirname)
    count=0
    for filename in filenames:
        if ".py" in filename:
            x=open(os.path.abspath(dirname + '/' + filename)).readlines()
            count=count+len(x)
    print "The number of lines of code in all python files is",count
line_count(sys.argv[1])
