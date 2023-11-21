#!/usr/bin/env python3

s = input()
sLen = len(s)
ascii = 0
i = 0
while i < sLen and not(ascii >= 65 and ascii <= 90):
   ascii = ord(s[i])
   i += 1
j = i - 1
while j < sLen and (ascii >= 65 and ascii <= 90):
   ascii = ord(s[j])
   if ascii >= 65 and ascii <= 90:
      j += 1
if not(i >= sLen) and j - i > 1:
   print(s[i - 1:j], i - 1)
