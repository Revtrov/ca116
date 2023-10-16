#!/usr/bin/env python3

n = int(input())
i = 1
while i <= n:
   if not (i % 15):
      print("fizz-buzz")
   elif not (i % 3):
      print("fizz")
   elif not (i % 5):
      print("buzz")
   else:
      print(i)
   i += 1
