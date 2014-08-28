def min(list):
	min = list[0]
	for elm in list[1:]:
	        if elm < min:     
			min = elm
	return "The minimum value in the list is: " + str(min)
def max(list):
	max = list[0]
	for elm in list[1:]:
		if elm > max:
	            max = elm
	return"The maximum value in the list is: " + str(max)
print min(['a','ax','nx','wq'])
print max([10,2,5,98])