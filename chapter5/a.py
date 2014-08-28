import os
import sys
def countfiles(files):
    return [file for file in files if '.py' in file]
files=os.listdir(sys.argv[1])
pyfile=countfiles(files)
print len(pyfile)
