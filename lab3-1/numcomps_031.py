#!/usr/bin/env python3

# use for loops and range to generate a list containing the numbers
# 1, 2, ... n
# n is an int from stdin

import sys

numbers = ([int(n.strip()) for n in sys.stdin])

def multiples(numbers):
	for number in numbers:
		# print(type(number))
		print("Multiples of 3:", [i for i in range(1, number + 1) if i % 3 == 0])
		print("Multiples of 3 squared:", [i * i for i in range(1, number + 1) if i % 3 == 0])
		print("Multiples of 4 doubled:", [i * 2 for i in range(1, number + 1) if i % 4 == 0])
		print("Multiples of 3 or 4:", [i for i in range(1, number + 1) if (i % 3 == 0) or (i % 4 == 0)])
		print("Multiples of 3 and 4:", [i for i in range(1, number + 1) if (i % 3 == 0) and (i % 4 == 0)])

	return None

multiples(numbers)

# python3 numcomps_031.py < numcomps_stdin_00_031.txt
# Multiples of 3: [3, 6]
# Multiples of 3 squared: [9, 36]
# Multiples of 4 doubled: [8, 16]
# Multiples of 3 or 4: [3, 4, 6, 8]
# Multiples of 3 and 4: []
# Multiples of 3: [3, 6, 9, 12]
# Multiples of 3 squared: [9, 36, 81, 144]
# Multiples of 4 doubled: [8, 16, 24]
# Multiples of 3 or 4: [3, 4, 6, 8, 9, 12]
# Multiples of 3 and 4: [12]