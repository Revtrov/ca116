#!/usr/bin/env python3

i = 0
while i < 10:
   equation = input()
   j = 0
   while j < len(equation) and equation[j] != "+":
      j += 1
   left = int(equation[0:j])
   right = int(equation[j + 1:])
   print(left + right)
   i += 1
