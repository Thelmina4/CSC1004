#!/usr/bin/env python3

# s/i = command line args
# s/o = echo those args back

import sys
args = sys.argv

i = 0
while i < len(args):
   print(args[i])
   i = i + 1
