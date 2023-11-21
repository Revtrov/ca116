#!/usr/bin/env python3

i = True
while i:
   equation = input()
   j = 0
   while j < len(equation) and equation[j] != "+":
      j += 1
   left = int(equation[:j])
   right = int(equation[j + 1:])
   sum = left + right
   print(sum)
   if sum == 1000:
      i = False
