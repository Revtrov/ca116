#!/usr/bin/env python3

import sys
args = sys.argv[1:]

with open(args[0], "w") as f:
   i = 1
   while i < len(args):
      f.write(args[i] + "\n")
      i += 1
