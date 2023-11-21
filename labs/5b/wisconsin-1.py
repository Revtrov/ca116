#!/usr/bin/env python3

data = input()
while data != "end":
   i = 0
   while i < len(data) and data[i] != ",":
      i += 1
   if data[i + 1:i + 3] == "WI" and data[:4] != "City":
      print(data[:i])
   data = input()
