#!/usr/bin/env python3

n = input()
nList = []
nCopy = []
while n != "end":
   nList.append(int(n))
   nCopy.append(int(n))
   n = input()
i = 0
index = 0
while i < len(nList):
   j = 0
   while j < len(nList):
      if nList[j] > nList[i]:
         temp = nList[i]
         nList[i] = nList[j]
         nList[j] = temp
      j += 1
   i += 1
i = 0
first = 1
while i < len(nList):
   if nList[0] == nCopy[i] and first:
      first = 0
      print(i)
   i += 1
