#!/usr/bin/env python3

n = int(input())
i = a = 0
b = 1
while i < n:
   b += a
   print(a)
   a = b - a
   i += 1
