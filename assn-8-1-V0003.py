#open the file
fname = raw_input("Enter the file name: ")
if len(fname) < 1 :
	fname = "romeo.txt"
	
try :
	fhand = open(fname)
except :
	print "Invalid file name"
	exit()
	
lst = list()

for line in fhand :
	line = line.rstrip()
	stuff = line.split()
	for word in stuff :
		if word not in lst :
			lst.append(word)
	
lst.sort()
print lst