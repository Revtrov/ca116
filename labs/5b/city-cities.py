#!/usr/bin/env python3

data = input()
while data != "end":
   city = ""
   i = 0
   while i < len(data) and data[i] != ",":
      i += 1
   city = data[:i]
   i = len(city) - 1
   lastWord = city[len(city) - 5:]
   if lastWord == " City":
      print(city)
   data = input()
