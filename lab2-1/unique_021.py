#!/usr/bin/env python3

# s/i = lines of text from stdin

# s/o = the number of unique words
# have to casefold()
# only .isalnum() is allowed

# s = "Hello, World! Python is amazing."
# # Create translation table
# import string
# translator = str.maketrans('', '', string.punctuation)
# # Remove punctuation
# clean_text = s.translate(translator)
# print(clean_text)

import sys

def remove(token):
	for char in token:
		if not char.isalnum():
			token = token.replace(char, "")
	return(token)

def unique(newlines):
	count = []
	for word in newlines:
		if 0 < len(word) and word not in count:
			count.append(word)
	return(len(count))

newlines = []

for lines in sys.stdin:
	line = lines.strip().casefold().split()
	for token in line:
		newlines.append(remove(token))

print(unique(newlines))