#!/usr/bin/env python3

headers = input()
j = True
i = 0
while j:
   oldI = i
   while i < len(headers) and headers[i] != ",":
      i += 1
   print(headers[oldI:i])
   i += 1
   if i > len(headers):
      j = False
