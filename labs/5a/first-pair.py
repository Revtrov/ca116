#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) - 1:
   if s[i] == s[i + 1] and s[i] != " ":
      print(s[i] * 2)
      i = len(s)
   i += 1
