cnt = 0
total = 0
avg = 0

while True :
	inp = raw_input('Enter a num: ')
	if inp == 'done' :	
		print total, cnt, avg
		break
	if len(inp) < 1 : 	continue
	
	try :
		num = float(inp)
	except :
		print('Invalid num!')
		continue

	cnt = cnt + 1
	total = total + num
	avg = total / cnt
	print total, cnt, avg
	
print('Done!')