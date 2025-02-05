#!/usr/bin/env python3

# s/i = text file w lines from sys.stdin

# remove anything that isn't isalnum
# check if its a palindrome

# s/o = True/False

import sys

def remove(line):
	for char in line:
		if not char.isalnum():
			line = line.replace(char, "")
	return(line)

def palindrome(newline):
	pal = True
	for i in range(0, len(newline)):
		if newline[i] != newline[len(newline) - i - 1]:
			pal = False
	return(pal)

for lines in sys.stdin:
	line = lines.strip().casefold()
	print(palindrome(remove(line)))
