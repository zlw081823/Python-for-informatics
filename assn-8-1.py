#open the file
fname = raw_input("Enter the file name:")
if len(fname) < 1 : 
	fname = "romeo.txt"

try :
	fhand = open(fname)
except :
	print "Invalid file name!"
	exit()
	
lst = list()

for line in fhand :
	line = line.rstrip()
	stuff = line.split()
	#print type(stuff)
	lst.extend(stuff)
	lst.sort()
	while True :
		print "IN THE LOOP !"
		flg = 0
		for num in range(len(lst) - 1) :
			if lst[num] == lst[num + 1] :
				print "Remove word :", lst[num]
				flg = 1
				removeWord = lst[num]
				break
		if flg == 0 :
			break
		else :
			lst.remove(removeWord)
print lst