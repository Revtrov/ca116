#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
totalHours = 0
while i < len(sList):
   sent = sList[i]
   sList[i] = sList[i].split(" ")
   if int(sList[i][2]) > 1:
      print(sent)
   i += 1
