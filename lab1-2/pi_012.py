#!/usr/bin/env python3

# s/i = ints from stdin in file

# s/o = print pi to that no in fancy format

from math import pi
import sys
for lines in sys.stdin:
   dpoint = int(lines.strip())
   # print(type(line))
   print(f"{pi:<.{dpoint:d}f}")
