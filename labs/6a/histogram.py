#!/usr/bin/env python3

n = input()
nList = [0] * 10
while n != "end":
   nList[int(n)] += 1
   n = input()
i = 0
while i < len(nList):
   print(str(i) + " " + nList[i] * "*")
   i += 1
