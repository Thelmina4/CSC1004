#!/usr/bin/env python3

# Assume an existing list of strings nameda

# s/o = writes the first non-empty string in a to standard output.

# test case
# a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
while i < len(a):
   if len(a[i]) >= 6:
      print(a[i])
   i += 1

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]
