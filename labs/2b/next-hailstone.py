#!/usr/bin/env python3

n = int(input())
if not (n % 2):
   n = n // 2
else:
   n = (3 * n) + 1
print(n)
