#!/usr/bin/env python3

s = input()
nString = ""
k = ""
i = 0
prev = True
while i < len(s):
   cN = ord(s[i])
   isLower = cN <= 122 and cN >= 97
   isUpper = cN <= 90 and cN >= 65
   if isLower:
      nString += chr(cN - 32)
   else:
      nString += s[i]
   i += 1
print(nString)
