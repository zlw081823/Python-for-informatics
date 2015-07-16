#Enter the file name
fname = raw_input("Enter file name:")
if len(fname) < 1 :
	fname = "mbox-short.txt"
	
try :
	fhand = open(fname)
except :
	print "Invalid file name!"
	exit()
	
cnt = 0
lst = list()

for line in fhand :
	if line.startswith("From ") :
		cnt += 1
		lst = line.rstrip().split()
		print lst[1]
		
print "There were", cnt, "lines in the file with From as the first word"