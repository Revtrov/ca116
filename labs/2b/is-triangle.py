#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
longest = 0
otherA = 0
otherB = 0
if a > b and a > c:
   longest = a
   otherA = b
   otherB = c
elif b > a and b > c:
   longest = b
   otherA = a
   otherB = c
else:
   longest = c
   otherA = b
   otherB = a
if longest - otherA - otherB < 0:
   print("yes")
else:
   print("no")
