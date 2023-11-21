#!/usr/bin/env python3

a = int(input())
b = int(input())
while b != 0:
   oldB = b
   b = a % b
   a = oldB
print(a)
