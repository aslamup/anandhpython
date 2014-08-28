import sys
import zipfile
z=zipfile.ZipFile(sys.argv[1],'w')
for i in range(2,len(sys.argv)):
 z.write(sys.argv[i])

