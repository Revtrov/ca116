#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
while i < len(sList):
   sList[i] = sList[i].split(" ")
   print(sList[i][3])
   i += 1
