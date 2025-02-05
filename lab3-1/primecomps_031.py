#!/usr/bin/env python3

# use for loops and range to generate a list containing the numbers
# 1, 2, ... n
# n is an int from stdin

# this time print primes only
# a prime is > 1 a

# python3 primecomps_031.py < primecomps_stdin_00_031.txt
# Primes: [2, 3, 5, 7]
# Primes: [2, 3, 5, 7, 11]

import sys

numbers = ([int(n.strip()) for n in sys.stdin])

def helper(d):
	for i in range(2, ((d // 2) + 1)):
		if d % i == 0:
			return False
	return True

def primes(numbers):
	for num in numbers:
		print("Primes:", [d for d in range(2, (num + 1)) if helper(d)])		
	return None

primes(numbers)
