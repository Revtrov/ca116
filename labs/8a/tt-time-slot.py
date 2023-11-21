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
   hour = int(sList[i][1])
   sList[i][1] = str(int(sList[i][1])) + ":00"
   tempA = sList[i][0:2]
   endT = str(hour + int(sList[i][2]) - 1) + ":50"
   tempB = sList[i][3:]
   sList[i] = tempA + [endT] + tempB
   sent = " ".join(sList[i])
   print(sent)
   i += 1
