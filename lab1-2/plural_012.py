#!/usr/bin/env python3

# s/i = text from stdin of nouns

# s/o =
# Add es if the noun ends in ch, sh, x, s or z.
# If a noun ends in a consonant + y drop the y and add ies.
# If a noun ends in f (or fe) drop the f (or fe) and add ves.
# If a noun ends in o add es.
# Otherwise add s.

import sys
es = "es"
vowel = "aeiou"

for lines in sys.stdin:
   line = lines.strip()
   ofe = line[len(line) - 1]
   # print(ofe)
   f = line[len(line) - 2]
   last2 = line[len(line) - 2:]
   # print(last2)
   # print(ofe, f)
   if ofe == "o":
      print(line + es)
   # f/fe - ves
   elif ofe == "f":
      print(line[:len(line) - 1] + "ves")
   elif f == "f" and ofe == "e":
      print(line[:len(line) - 2] + "ves")
   elif last2 == "ch" or last2 == "sh" or ofe == "x" or ofe == "s" or ofe == "z":
      print(line + es)
   elif f not in vowel and ofe == "y":
      print(line[:len(line) - 1] + "ies")
   else:
      print(line + "s")
