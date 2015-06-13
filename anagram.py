count=int(raw_input())

for i in range(count):
	print i
	string=raw_input().split()

	
	if len(string[0])!=len(string[1]):
		print 'NO'

	else:
		summation1=0
		summation2=0
		for i in string[0]:
			summation1=ord(i)+summation1
		for j in string[1]:
			summation2=ord(j)+summation2

		if summation2==summation1:
			print 'YES'
		else:
			print 'NO'
	