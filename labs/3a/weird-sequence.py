#!/usr/bin/env python3

n = int(input())
i = 0
while i < n:
   isEven = -(i % 2)
   print(i * ((not isEven) + isEven))
   i += 1
