#!/usr/bin/env python3

# s/i= txt from stdin
#     there is a number on one line
#     and then bert response

# s/o = bert can be trusted or not

# cat guess_stdin_00_022.txt
# 5
# higher
# 10
# higher
# 18
# lower
# 15
# correct

import sys

# [1::2]

lines = []
for line in sys.stdin:
	lines.append(line.rstrip())
guess, bert = lines[::2], lines[1::2]

ans = int(guess[-1])

# print(guess, bert)
high = "higher"
low = "lower"
maxg = 20
ming = 0
for i in range(0, len(guess[:-1])):
   ernie = int(guess[i])

   if bert[i] == high and ernie > ming:
      ming = ernie
      # print(ming, "ming", ernie, "ernie")

   elif bert[i] == low and ernie < maxg:
      maxg = ernie
      # print(maxg, ": maxg", ernie, ": ernie")

# print(ming, maxg)
if ans in range(ming, maxg):
   print("Bert can be trusted")
else:
   print("Bert is not to be trusted")
