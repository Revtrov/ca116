#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
i = 0
while i < len(sList):
   sent = sList[i]
   sList[i] = sList[i].split(" ")
   if int(sList[i][0]) == 3:
      print(sent)
   i += 1
