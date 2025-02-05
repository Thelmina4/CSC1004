#!/usr/bin/env python3

# s/i = lines of text from stdin
# each line = single string

# s/o = each string minus the 1st and last chars

import sys

for lines in sys.stdin:
	line = lines.strip()
	chopped = line[1:len(line) - 1]
	if chopped:
		print(chopped)
