#!/usr/bin/env python3

# s/i = text file w pairs of words
#       one pair per line

# write a program that compares the letters in each string and removes it one time
# until the second string is empty

# s/o = True is they match, are anagrams of each other

import sys

def anagram(string0, string1):
	matched = True
	for char in string0:
		if char in string1:
			string1 = string1.replace(char, "", 1)
			string0 = string0.replace(char, "", 1)
	if not(len(string0) == 0 and len(string1) == 0):
		matched = False
	# print(string0, string1)

	return(matched)

for lines in sys.stdin:
	line = lines.strip().split()
	# print(line)
	# tokens = list(line)
	# print(tokens)
	print(anagram(line[0], line[1]))

