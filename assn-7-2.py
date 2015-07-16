fname = raw_input('Enter the file name: ')

#set default value
if len(fname) == 0 :
	fname = 'mbox-short.txt'

try :
	fhand = open(fname)
except :
	print 'Invalid file name!'
	exit()
	
cnt = 0.0
avg = 0.0

for line in fhand :
	if line.startswith('X-DSPAM-Confidence:') :
		cnt = cnt + 1
		num = line.find(':')
		avg += float(line[num + 1:])

avg /= cnt
print 'Average spam confidence:', avg