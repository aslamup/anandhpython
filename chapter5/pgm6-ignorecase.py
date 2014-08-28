#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

import sys
import os
def line_count(dirname):
    for root,dirs,filenames in os.walk(dirname):
        for filename in filenames:
            if ".py" in filename:
                yield os.path.join(root,filename)
paths=line_count(sys.argv[1])
count = 0
for path in paths:
    for line in open(path).readlines():
        if((line[0] !='#') and (line.strip()!='')):
            count +=1
print "The total number of lines of code, ignoring empty and comment lines, in all python files is", count
