#!/usr/bin/env python3

# s/i = 2 lines in text in a file
#       the first line is numbers
#       the second line is A, B and C

import sys

lines = sys.stdin.readlines()
nums, ABC = lines[0].strip().split(), lines[1].strip()
int_nums = []
for c in nums:
	int_nums.append(int(c))
int_nums.sort()
A, B, C = int_nums[0], int_nums[1], int_nums[2]

new_nums = []
for letter in ABC:
	if letter == "A":
		new_nums.append(str(A))
	elif letter == "B":
		new_nums.append(str(B))
	else:
		new_nums.append(str(C))

print(" ".join(new_nums))
