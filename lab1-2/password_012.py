#!/usr/bin/env python3

# s/i = text from stdin
# the lines are made up of:
# - upper chars,
# - lower chars,
# - ints,
# - special chars eg {[(%^& (everything else)

import sys
for lines in sys.stdin:
   line = lines.strip()
   #print(lines)
   lower = 0
   upper = 0
   char = 0
   d = 0
   for c in line:
      if c.islower():
         lower = 1
      elif c.isupper():
         upper = 1
      elif int(c.isdigit()):
         d = 1
      else:
         char = 1
   print(lower + upper + d + char)

