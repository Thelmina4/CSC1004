#!/usr/bin/env python3

# Assume an existing list of strings nameda

# s/o = writes the first word that is len 6 or longer

# test case
# a = ['cat', 'elephant', 'mouse', 'lizard', 'horse', 'mongoose']elephant

# a = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
# abcdef

# a = ['87654321', '7654321', '654321', '54321', '4321', '321', '21', '2']
# 87654321

# a = ['', '', '', '', '', '', '', '', '', '']

# a = []

# a = ['mongoose']
# mongoose

# a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

i = 0
while i < len(a) and len(a[i]) < 6:
   i += 1

if i != len(a):
   print(a[i])

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]
