largest = None
smallest = None

while True :
	inp = raw_input('Enter a num: ')
	if inp == 'done' : 	break
	if len(inp) < 1 : 	continue
	
	try :
		num = float(inp)
	except :
		print 'Invalid num !'
		continue
	
	if largest is None and smallest is None :
		largest = num
		smallest = num
	elif num > largest :
		largest = num
	elif num < smallest :
		smallest = num
		
print 'Maximum', largest
print 'smallest', smallest