#!/usr/bin/env python3

# s/i = lines of text from stdin
# each line = student email address

import sys

for lines in sys.stdin:
	line = lines.strip().split("@")
	# print(line)
	tokens = line[0].split(".")
	# print(tokens)
	for char in tokens[1]:
		if not char.islower():
			tokens[1] = tokens[1].replace(char, "")

	# print(tokens)
	newline = "" 
	for token in tokens:
		token = token[0].capitalize() + token[1:len(token)] + " "
		newline += token
	print(newline[:len(newline) - 1])
