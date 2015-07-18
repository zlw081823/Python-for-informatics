#open the file
fname = raw_input("Enter file name:")
if len(fname) < 1 :	fname = "mbox-short.txt"
try :
	fhand = open(fname)
except :
	print "Invalid file name!"
	exit()
	
lst = list()
sender = dict()
for line in fhand :
	if "From " in line :
		lst = line.rstrip().split()
		sender[lst[1]] = sender.get(lst[1], 0) + 1
		
maxCnt = None
maxName = None
for name, cnt in sender.items() :
	if maxName is None or maxCnt < cnt :
		maxName = name
		maxCnt = cnt
		
print maxName, maxCnt