#!/usr/bin/env python3

s = input()
flat = ""
i = 0
while i < len(s):
   c = s[i]
   isLower = c <= "z" and c >= "a"
   isUpper = c <= "Z" and c >= "A"
   if isUpper:
      flat += chr(ord(c) + 32)
   else:
      flat += s[i]
   i += 1
k = ""
i = 0
j = 0
while i < len(flat):
   c = flat[i]
   isChar = c <= "z" and c >= "a"
   if j % 2 and c != " " and isChar:
      k += chr(ord(c) - 32)
   else:
      k += c
   if ord(c) != 32 and isChar:
      j += 1
   i += 1
print(k)
