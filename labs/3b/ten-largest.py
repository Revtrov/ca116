#!/usr/bin/env python3

iterations = 10
max = 0
i = 0
while i < iterations:
   n = int(input())
   if n > max or max == 0:
      max = n
   i += 1
print(max)
