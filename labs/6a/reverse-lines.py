#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
while i < len(sList):
   print(sList[len(sList) - i - 1])
   i += 1
