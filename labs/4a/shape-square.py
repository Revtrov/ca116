#!/usr/bin/env python3

n = int(input())
line = "*" * n
print(line)
i = 0
while i < n - 2:
   print("*" + ((" ") * (n - 2)) + "*")
   i += 1
if n > 1:
   print(line)
