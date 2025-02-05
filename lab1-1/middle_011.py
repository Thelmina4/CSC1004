#!/usr/bin/env python3

# s/i = lines of text from stdin
# each line = single string

# s/o = middle char of each str
# else print("No middle character!")

import sys
for lines in sys.stdin:
	line = lines.strip()
	if len(line) % 2 == 1:
		middle = len(line) // 2
		# print(middle)
		print(line[len(line) // 2])
	else:
		print("No middle character!")
