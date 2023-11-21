#!/usr/bin/env python3

s = input()
isFloat = False
sign = ""
trailing = ""
if s[0] == "-":
   s = s[1:len(s)]
   sign = "-"
if s[0] == ".":
   s = "0" + s
if s[-1] == ".":
   trailing = "0"
i = 0
j = False
while i < len(s) and not j:
   if s[i] != ".":
      i += 1
   elif s[i] == ".":
      isFloat = True
      j = True
if isFloat:
   print(sign + s + trailing)
else:
   print(sign + s + ".0")
