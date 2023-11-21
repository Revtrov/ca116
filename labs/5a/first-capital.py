#!/usr/bin/env python3

s = input()
ascii = 0
i = 0
while i < len(s) and not(ascii >= 65 and ascii <= 90):
   ascii = ord(s[i])
   if not(ascii >= 65 and ascii <= 90):
      i += 1
if ascii >= 65 and ascii <= 90:
   print(chr(ascii), i)
