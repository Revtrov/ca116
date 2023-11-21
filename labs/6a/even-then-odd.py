#!/usr/bin/env python3

s = input()
evens = []
odds = []
while s != "end":
   if not(int(s) % 2):
      evens.append(int(s))
   else:
      odds.append(int(s))
   s = input()
i = 0
while i < len(evens):
   print(evens[i])
   i += 1
i = 0
while i < len(odds):
   print(odds[i])
   i += 1
