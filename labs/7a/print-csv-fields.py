#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
n = int(input())
j = 0
while j < len(sList):
   p = 0
   i = 0
   oldI = 0
   while p <= n:
      while i < len(sList[j]) and sList[j][i] != ",":
         i += 1
      if p == n:
         print(sList[j][oldI:i])
      i += 1
      oldI = i
      p += 1
   j += 1
