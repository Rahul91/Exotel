# Exotel

#1. Anagram
  An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once

Solution 1 : Agreegate the acsii value for letters of given probable anagrams, if there length and value of summation is same, they are anagram

Soulton 2 : Sort and campare, if equal, then anagram


#2. T9 Texting
T9 which stands for Text on 9 keys, is a USA-patented[1] predictive text technology for mobile phones (specifically those that contain a 3x4 numeric keypad)

Solution 1 : keypad-mapping is done using a Dictionary, then aggregating all the alphabets, corresponding to each keystroke, for example, 2,2,8 would give like
	 2: abc
	 2: abc
	 8: tuv
Therefore, 2,2,8 would give abcabctuv, now, taking all permutations of this would be our list of all_permuation, now we will 
iterate this list to find the pattern matching. If we get hit, we break, and store that hit in an list, after all the iteration 
we will sort the list and print one by one as output.

Solution 2 : Iterating reverse in the keystroke list, therefore key-stroke='2,2,8', when iterated reversed, 8 is the first object, all the 
letter/alphabets corresponding to '8' are aggregated, then this process is repeated untill first key-stroke is reached. When first key-stroke
is reached, we take a permutation of all the agrregated letters, then we iterate through the list, adding the letters corresponding to first
key-stroke to the beggining of each element, so the list we got after adding the corresponding letter to each element to the list is the final
all_permuation list, then we iterate this all_permutation list to find the pattern matching. If we get hit, we break, and store that hit in an list, after all the iteration 
we will sort the list and print one by one as output. 


