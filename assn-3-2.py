try:
	score = raw_input("Enter Score:")
	s = float(score)
except:
	print("Please enter a number!")
	quit()

if s <= 1 and s >= 0:
	if s < 0.6:
		print("F")
	elif s < 0.7:
		print("D")
	elif s < 0.8:
		print("C")
	elif s < 0.9:
		print("B")
	else:
		print("A")
else:
	print("Enter a number between 0 and 1!")
	quit()