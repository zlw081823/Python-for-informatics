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
	#print "Loop 1"
	line = line.rstrip()
	stuff = line.split()
	for word in stuff :
		#print "Loop 2"
		if len(lst) < 1 :
			#print "Add first number"
			lst.append(word)
		else :
			cnt = 0
			for lstWord in lst :
				#print "Loop 3"
				if word != lstWord :
					cnt += 1
					#print "word is:", word, "lstWord is:", lstWord, "cnt is:", cnt
					if cnt == len(lst) :
						#print "Add word:", word
						lst.append(word)
						cnt = 0
					else :
						continue
				else :
					break
	
lst.sort()
print lst