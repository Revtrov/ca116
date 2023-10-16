#!/usr/bin/env python3

n = int(input())
a = 0
b = 1
while a < n:
   b += a
   print(a)
   a = b - a
