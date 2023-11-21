#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
while i < len(sList):
   print(str(i) + " " + str(len(sList)) + " " + sList[i])
   i += 1
