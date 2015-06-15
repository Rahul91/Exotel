import itertools

keypad_mapping ={
	'2' : ['a','b','c'],
	'3' : ['d','e','f'],
	'4' : ['g','h','i'],
	'5' : ['j','k','l'],
	'6' : ['m','n','o'],
	'7' : ['p','q','r','s'],
	'8' : ['t','u','v'],
	'9' : ['w','x','y','z']
}

keystroke=raw_input().split(',')      #mobile key-stroke, example : 2,2,8
len_keystroke=len(keystroke)

words=raw_input().split(',')          #Words to be find, example : cat,rat,bat,exotel
count=len(words)						#total no. of words

appended_letter=''						#initializing a string
all_permutation=[]						#initializing a list

j=0
for i in reversed(keystroke):
	letter=keypad_mapping[i]
	if (j+1)!=len_keystroke:
		letter=keypad_mapping[i]
		for x in letter:
			appended_letter=appended_letter+x  										# addiditon of all possible letters from key-stroke, for example if 2,2 is pressed,
		permutation=list(map("".join, itertools.permutations(appended_letter)))
		j+=1									 
	else:
		p=0
		for x in letter:
			for i in permutation:
				i=x+i
				all_permutation.insert(p,i)
				p+=1

list_show=[]
for i in range(len(words)):					#Login to check if any given input word is present in all possible combination
	for word in all_permutation:
		if words[i] in word:
			list_show.append(words[i])		#found a match 
			break
		else:
			pass

sorted_list_show=sorted(list_show)
for output in sorted_list_show:
	print output							#printting the output


