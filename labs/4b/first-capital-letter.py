#!/usr/bin/env python3

s = input()
i = 0
position = 0
while i < len(s):
   position = i
   if ord(s[i]) <= 88 and ord(s[i]) >= 65:
      i = len(s)
   i += 1
print(position)
