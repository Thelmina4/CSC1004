#!/usr/bin/env python3

# Assume an existing list of strings nameda

# s/o = writes the first non-empty string in a to standard output.

# test case
# a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
while i < len(a) and a[i] == "":
   i += 1

if i != len(a):
   print(a[i])

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]
