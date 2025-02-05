#!/usr/bin/env python3

# s/i = words, one / line into stdin


import sys
words = [word.strip() for word in sys.stdin]
# print(words)

def Q_q(word):
   if word[-1] in "qQ":
      return word
   elif len(word) > 1:
      for i in range(0, len(word) - 1):
         if word[i] in "qQ" and word[i + 1] not in "Uu":
            return word
   # else:
   #    return None

print("Words with q but no u:", [word for word in words if Q_q(word)])

# python3 qnou_031.py < qnou_stdin_00_031.txt
# print(len(['Colloq', 'IQ', 'Iraq', 'Iraqi', 'q', 'Qatar', 'QED', "q's", 'seq']))
