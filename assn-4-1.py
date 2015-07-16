def computePay (h, r) :
	if h > 40 :
		p = 40 * r + (h - 40) * r * 1.5
	else :
		p = 40 * r
	return p

try :
	inp = raw_input("Enter hour:")
	hour = float(inp)
	inp = raw_input("Enter rate:")
	rate = float(inp)
except :
	print "Please enter a number"
	quit()

pay = computePay(hour, rate)
print pay