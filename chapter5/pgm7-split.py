#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.
import sys
def split(n,filename):
    f=open(filename).readlines()
    x=len(f)/int(n)
    j=0
    if len(f)%int(n)==0:
        for i in range(x):
            f1=open('%d.txt'%i,'w')
            f1.writelines(f[j*int(n):(j+1)*int(n)])
            j +=1
            f1.close()
    else:
        for i in range(x+1):
            f1=open('%d.txt'%i,'w')
            f1.writelines(f[j*int(n):(j+1)*int(n)])
            j +=1
            f1.close()
split(sys.argv[1],sys.argv[2])
