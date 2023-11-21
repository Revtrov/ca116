#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and s[i] != " ":
   i += 1
day = s[:i]
i += 1
j = i
while i < len(s) and s[i] != " ":
   i += 1
dayNum = s[j:i]
j = i + 1
while i < len(s) and s[i] != ",":
   i += 1
month = s[j:i]
year = s[len(s) - 4:len(s)]
print(month + " " + dayNum + ", " + year + " (" + day + ")")
