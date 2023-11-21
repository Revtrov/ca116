#!/usr/bin/env python3

n = int(input())
base = 16
hex = ""
digits = "0123456789abcdef"
while n > 0:
   hex = digits[n % base] + hex
   n = n // base
ascii = 0
i = 0
while i < len(hex) and not(ascii >= 97 and ascii <= 122):
   ascii = ord(hex[i])
   if not(ascii >= 97 and ascii <= 122):
      i += 1
if (ascii >= 97 and ascii <= 122):
   print(chr(ascii))
