#!/usr/bin/env python3

# s/i = takes in a filename as a command arguement sys.argv[1]
#     inside the file, each line = score and the student name

# s/o = print out the name of the stuent that scores the highest marks
#       print the score on the next line
#       where there is a joint best score, print the first encounter

import sys

def best(lines):
	best_score = 0
	name = []
	for line in lines:
		line = line.rstrip().split()
		score = int(line[0])
		if score > best_score:
			best_score = score
			name.append(" ".join(line[1:]))
	print("Best student:", name[-1])
	print("Best mark:", best_score)
	return None

with open(sys.argv[1], "r") as f:
	lines = f.readlines()

best(lines)
