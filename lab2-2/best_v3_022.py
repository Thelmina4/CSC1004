#!/usr/bin/env python3

# s/i = takes in a filename as a command arguement sys.argv[1]
#     inside the file, each line = score and the student name

# s/o = same same to the last 1, but this time must handle exceptions
#       for non intergers in the score

import sys

def best(lines):
	best_score = 0
	name = []
	for line in lines:
		line = line.rstrip().split()
		try:
			score = int(line[0])
			if score > best_score:
				best_score = score
				name.append(" ".join(line[1:]))
		except (ValueError):
			(print(f"Invalid mark {line[0]} encountered. Skipping."))
	print("Best student:", name[-1])
	print("Best mark:", best_score)
	return None

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

best(lines)
