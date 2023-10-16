#!/usr/bin/env python3

total = 0
i = 0
while i < 10:
   n = int(input())
   total += (1 - (n % 2)) * n
   i += 1
print(total)
