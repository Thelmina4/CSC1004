#!/usr/bin/env python3

# Assume an existing list of words (strings) a
# and another str s

# s/o = rites each word in a for which s is a prefix
# one per line.

# a = ['mountain', 'montagne', 'mont', 'mo', 'montages', 'zebra', 'monthly']
# s = mont
# montagne
# mont
# montages
# monthly

# a = ['ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
# s = "abc"
# abc

# a = ['dog', 'cat', 'mouse']
# s =

# a = []
# s = mongoose

# a = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
# s = 1

# b = "mountain"
# print(b[:4])

i = 0
while i < len(a):
   if a[i][:len(s)] == s:
      print(a[i])
   i += 1

if __name__ == "__main__":
   a = ["dog", "cat", "mouse"]
