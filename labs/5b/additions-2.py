#!/usr/bin/env python3

sum = 0
equation = input()
eLen = len(equation)
i = 0
j = 0
while i < 5:
   prevJ = j
   while j < eLen and equation[j] != "+":
      j += 1
   sum += int(equation[prevJ:j])
   j += 1
   i += 1
print(sum)
