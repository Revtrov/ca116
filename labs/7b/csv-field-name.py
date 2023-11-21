#!/usr/bin/env python3

import sys
n = int(sys.argv[1])
sList = [input()]
p = 0
i = 0
oldI = 0
while p <= n:
   while i < len(sList[0]) and sList[0][i] != ",":
      i += 1
   if p == n:
      print(sList[0][oldI:i])
   i += 1
   oldI = i
   p += 1
