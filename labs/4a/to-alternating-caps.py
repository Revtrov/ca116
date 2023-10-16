#!/usr/bin/env python3

s = input()
l = ""
i = 0
prev = True
while i < len(s):
   cN = ord(s[i])
   isLower = cN <= 122 and cN >= 97
   isUpper = cN <= 90 and cN >= 65
   print(prev)
   if isUpper and prev:
      l += chr(cN + 32)
      prev = False
   if isLower and not prev:
      l += chr(cN - 32)
      prev = True
   i+=1
print(l)
print(ord("Z"))
