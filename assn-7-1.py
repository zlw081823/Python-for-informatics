fname = raw_input('Enter the file name: ')

#set default value
if len(fname) == 0 :
	fname = 'words.txt'

try :
	fhand = open(fname)
except :
	print 'File did not exist!'
	exit()

for line in fhand :
	line  = line.rstrip().upper()
	print line