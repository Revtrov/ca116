#!/usr/bin/env python3

nA = input()
nAList = []
while nA != "end":
   nAList.append(int(nA))
   nA = input()
nB = input()
nBList = []
while nB != "end":
   nBList.append(int(nB))
   nB = input()
mergedList = []
i = 0
while i < len(nAList):
   mergedList.append(nAList[i])
   i += 1
i = 0
while i < len(nBList):
   mergedList.append(nBList[i])
   i += 1
i = 0
while i < len(mergedList):
   j = 0
   while j < len(mergedList):
      if mergedList[i] < mergedList[j]:
         temp = mergedList[i]
         mergedList[i] = mergedList[j]
         mergedList[j] = temp
      j += 1
   i += 1
i = 0
while i < len(mergedList):
   print(mergedList[i])
   i += 1
