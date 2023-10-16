#!/usr/bin/env python3

n = int(input())
nLen = len(str(n))
m = 0
i = 0
while i < nLen:
   power = 10 ** i
   digit = ((n % (10 ** (i + 1)) - (n % power))) // power
   m += digit * (10 ** (nLen - i - 1))
   i += 1
if n - m == 0:
   print("yes")
else:
   print("no")
