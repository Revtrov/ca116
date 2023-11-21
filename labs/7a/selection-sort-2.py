#!/usr/bin/env python3

n = input()
nList = []
nListCopy = []
while n != "end":
   nList.append(int(n))
   nListCopy.append(int(n))
   n = input()
endN = int(input())
nList = nListCopy[endN:]
i = 0
while i < len(nList) - 1:
   j = i + 1
   while j < len(nList):
      if nList[i] > nList[j]:
         temp = nList[i]
         nList[i] = nList[j]
         nList[j] = temp
      j += 1
   i += 1
i = len(nListCopy) - 1
while i > 0 and nList[0] != nListCopy[i]:
   i -= 1
print(i)
