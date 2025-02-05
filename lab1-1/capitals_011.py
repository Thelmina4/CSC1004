#!/usr/bin/env python3

# s/i = read lines of text from stdin
# each line is a string and contains at least 2 letters

# s/o = caps for the 1st and last letter

import sys

for lines in sys.stdin:
	line = lines.strip()
	# print(line)
	print(line[0].capitalize() + line[1:len(line) - 1] + line[len(line) - 1].capitalize())
