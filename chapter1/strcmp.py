# to compare two strings whether thet are equal or not

def istrcmp(x,y):
 if x.lower()==y.lower():
  print 'Strings are equal'
 else:
  print 'Strings are not equal'
str1=raw_input("Enter the first string:")
str2=raw_input("Enter the second string:")
istrcmp(str1,str2)

