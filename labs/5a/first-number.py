#!/usr/bin/env python3

s = input()
sLen = len(s)
ascii = 0
i = 0
while i < sLen and not(ascii >= 48 and ascii <= 57):
   ascii = ord(s[i])
   i += 1
j = i - 1
while j < sLen and (ascii >= 48 and ascii <= 57):
   ascii = ord(s[j])
   if ascii >= 48 and ascii <= 57:
      j += 1
if not(i >= sLen) and j - i > 1:
   print(s[i - 1:j], i - 1)
