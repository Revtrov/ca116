#!/usr/bin/env python3

s = str(input())
note = ""
i = 0
while i < len(s):
   if ord(s[i]) >= 97 and ord(s[i]) <= 103:
      note = s[i]
      i = len(s)
   i += 1
print(note)
