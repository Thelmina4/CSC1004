#!/usr/bin/env python3

# s/i = read lines from stdin
# each line  = 2 strings

# s/o = True if each char in the first str is in 2nd str

# txt = "I like bananas"

# x = txt.replace("bananas", "apples")

# print(x)

import sys
for lines in sys.stdin:
	line = lines.strip().lower().split()
	# print(line)
	tokens = list(line)
	matched = True
	for char in line[0]:
		if char in line[1]:
			line[1] = line[1].replace(char, '')
		else:
			matched = False
	print(matched)
