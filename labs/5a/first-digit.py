#!/usr/bin/env python3

s = input()
ascii = 0
i = 0
while i < len(s) and not(ascii >= 48 and ascii <= 57):
   ascii = ord(s[i])
   if not(ascii >= 48 and ascii <= 57):
      i += 1
if ascii >= 48 and ascii <= 57:
   print(chr(ascii), i)
