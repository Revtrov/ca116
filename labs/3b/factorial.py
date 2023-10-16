#!/usr/bin/env python3

n = int(input())
factorial = 1
i = 0
while i < n:
   factorial *= i + 1
   i += 1
print(factorial)
