#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   inList = 0
   j = 0
   while j < len(sList):
      if sList[j] == s:
         inList = 1
      j += 1
   if not inList:
      sList.append(s)
   s = input()
i = 0
while i < len(sList):
   print(sList[i])
   i += 1
