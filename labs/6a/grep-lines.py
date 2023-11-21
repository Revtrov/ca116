#!/usr/bin/env python3

import sys
args = sys.argv[1:]
s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
while i < len(sList):
   j = 0
   found = 0
   while j < len(sList[i]) - len(args[0]) + 1:
      if sList[i][j:j + len(args[0])] == args[0]:
         if not found:
            print(sList[i])
         found = 1
      j += 1
   i += 1
