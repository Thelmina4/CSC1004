#!/usr/bin/env python3

# s/i = eg Nobody expects the Spanish inquisition.

# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# |                                                  |
# v                                                  v
# nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM

# creat a cypher, using a dictionary to encrypt the input

# s/o = the cyphered line

import sys

s = sys.stdin.readlines()
# print(s)

cypher = {}

line1 = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").strip()
line2 = ("nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM").strip()
# print(line1, line2)

i = 0
while i < len(line1):
   letter, cyph = line1[i], line2[i]
   cypher[letter] = cyph
   i += 1
# print(cypher)

new_lines = []
j = 0
while j < len(s):
   line = s[j].strip()
   # print(line)
   new_line = []
   k = 0
   while k < len(line):
      inp = line[k]
      # print(inp)
      if inp in cypher:
         new_line.append(cypher[inp])
      else:
         new_line.append(inp)
      k += 1
   new_lines.append("".join(new_line))
   j += 1

# print(new_lines)
k = 0
while k < len(new_lines):
   print(new_lines[k])
   k += 1
