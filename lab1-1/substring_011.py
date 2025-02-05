#!/usr/bin/env python3

# s/i = lines of text from stdin
# each line = 2 x strings

# s/o = True if the first string is a substring of the second string
# differences in case can be ignored

import sys

for lines in sys.stdin:
	line = lines.strip().lower().split()
	print(line[0] in line[1])