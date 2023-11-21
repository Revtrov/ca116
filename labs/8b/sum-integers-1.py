#!/usr/bin/env python3

import sys

with sys.stdin as f:
   lines = f.readlines()
   tot = 0
   i = 0
   while i < len(lines):
      tot += int(lines[i])
      i += 1
   print(tot)
