import re
test_input = raw_input("Enter the phone number")
if re.match(r'^(\d{10})$', test_input):
	print ('That is a valid phone number')
else:
	print ('This is not a valid phone number')
