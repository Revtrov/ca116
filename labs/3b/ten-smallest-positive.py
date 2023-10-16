#!/usr/bin/env python3

iterations = 10
min = 0
i = 0
while i < iterations:
   n = int(input())
   if (n < min and n > 0) or i == 0:
      min = n
   i += 1
print(min)
