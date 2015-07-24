#open file 
fname = raw_input("Enter file name:")
if len(fname) < 1 :
	fname = "mbox-short.txt"
try :
	fhand = open(fname)
except :
	print "Invalid file name!"
	exit()
	
hour = dict()
for line in fhand :
	if "From " not in line :
		continue
	words = line.split()
	time = words[5].split(":")
	hour[time[0]] = hour.get(time[0],0) + 1
	
hrs = hour.items()
print hrs
hrs.sort()

for key, value in hrs :
	print key, value