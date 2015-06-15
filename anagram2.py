count=int(raw_input())

for i in range(count):
	string=raw_input().split()
	
	if len(string[0])!=len(string[1]):
		print 'NO'

	else:
		#print (string[0]., sorted(string[1])
		#a=''.join(sorted(string[0]))
		#b=''.join(sorted(string[1]))
		if ((''.join(sorted(string[0])))==(''.join(sorted(string[1])))):
			print 'YES'
		else:
			print 'NO'
	