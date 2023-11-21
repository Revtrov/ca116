#!/usr/bin/env python3

n = input()
numbers = []
while n != "end":
   numbers.append(n)
   n = input()
   if n != "end":
      n = int(n)
m = int(input())
i = 0
while i < len(numbers):
   print(m + int(numbers[i]))
   i += 1
