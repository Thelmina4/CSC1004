#!/usr/bin/env python3

# s/i = lines from std in

# s/o fancy formated centred

import sys

lines = sys.stdin.readlines()

maxl = 0
for line in lines:
   if maxl < len(line.strip()):
      maxl = len(line.strip())
# print(max)

for line in lines:
   # print(line.strip())
   print(f"{line.strip():^{maxl:d}s}")
