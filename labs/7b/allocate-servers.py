#!/usr/bin/env python3

arrTimeList = []
arrTime = input()
while arrTime != "end":
   arrTimeList.append(int(arrTime))
   arrTime = input()
serversRunning = 0
serversNeeded = 0
firstServer = 0
i = 0
j = 0
while j < len(arrTimeList):
   while i < len(arrTimeList):
      if arrTimeList[i] - arrTimeList[j] < 1000:
         serversRunning += 1
      i += 1
   j += 1
print(serversNeeded)
