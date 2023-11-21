#!/usr/bin/env python3

n = input()
nList = []
while n != "end":
   nList.append(int(n))
   n = input()
i = 0
while i < len(nList):
   j = 0
   while j < len(nList):
      if nList[j] > nList[i]:
         temp = nList[i]
         nList[i] = nList[j]
         nList[j] = temp
      j += 1
   i += 1
print(nList[(len(nList) // 2) + (len(nList) % 1)])
