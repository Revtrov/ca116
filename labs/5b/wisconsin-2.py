#!/usr/bin/env python3

data = input()
count = 0
while data != "end":
   i = 0
   while i < len(data) and data[i] != ",":
      i += 1
   if data[i + 1:i + 3] == "WI" and data[:4] != "City":
      count += 1
   data = input()
print(count)
