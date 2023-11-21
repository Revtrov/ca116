#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
totalHours = 0
while i < len(sList):
   sList[i] = sList[i].split(" ")
   totalHours += int(sList[i][2])
   i += 1
print(totalHours)
