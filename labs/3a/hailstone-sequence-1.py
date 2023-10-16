#!/usr/bin/env python3

n = int(input())
m = int(input())
i = 0
while i < n:
   print(m)
   if not (m % 2):
      m = m // 2
   else:
      m = (m * 3) + 1
   i += 1
