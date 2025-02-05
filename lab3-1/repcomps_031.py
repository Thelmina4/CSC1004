#!/usr/bin/env python3

# use for loops and range to generate a list containing the numbers
# 1, 2, ... n
# n is an int from stdin

# this time the list will be len(n)
# with the numbers replaced

import sys

numbers = ([int(n.strip()) for n in sys.stdin])

def multiples(numbers):
	for number in numbers:
		print("Non-multiples of 3 replaced:", [i if i % 3 == 0 else 0 for i in range(1, number + 1)])
		
	return None

multiples(numbers)

# python3 repcomps_031.py < repcomps_stdin_00_031.txt
# Non-multiples of 3 replaced: [0, 0, 3, 0, 0, 6, 0, 0]
# Non-multiples of 3 replaced: [0, 0, 3, 0, 0, 6, 0, 0, 9, 0, 0, 12]