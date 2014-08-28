import sys
import os
def list_all_files_in_directory(dirname):
	filenames = os.listdir(dirname)
	for filename in filenames:
		print filename
print list_all_files_in_directory(sys.argv[1])
