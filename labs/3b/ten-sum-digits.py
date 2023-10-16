#!/usr/bin/env python3

total = 0
i = 0
while i < 10:
   n = int(input())
   if n < 0:
      total += -n % 10
   else:
      total += n % 10
   i += 1
print(total)
