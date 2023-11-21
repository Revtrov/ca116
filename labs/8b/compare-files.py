#!/usr/bin/env python3

import sys

args = sys.argv[1:]
aFile = args[0]
bFile = args[1]
aLines = []
bLines = []
with open(aFile, 'r') as a:
   line = a.readline()
   while line != "":
      aLines.append(line)
      line = a.readline()
with open(bFile, 'r') as b:
   line = b.readline()
   while line != "":
      bLines.append(line)
      line = b.readline()
interrupt = False
i = 0
while i < len(aLines) and i < len(bLines) and not interrupt:
   if len(aLines) != len(bLines):
      if len(aLines) < len(bLines):
         print(len(aLines), 0)
      else:
         print(len(bLines), 0)
      interrupt = True
   j = 0
   while j < len(aLines[i]) and j < len(bLines[i]):
      if aLines[i][j] != bLines[i][j]:
         interrupt = True
         print(i, j)
      j += 1
   i += 1
