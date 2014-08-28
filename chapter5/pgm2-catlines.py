# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
import sys
filenames=[]
for i in range(1,len(sys.argv)):
        filenames.append(sys.argv[i])
def cat_lines(filenames):
            for f in filenames:
                   for line in open(f):
                        if len(line)>40:
                            yield line
a=cat_lines(filenames)
for i in a:
    print i
