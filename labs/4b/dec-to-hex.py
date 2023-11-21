#!/usr/bin/env python3

n = int(input())
base = 16
s = ""

digits = "0123456789abcdef"

while 0 < n:
   s = digits[n % base] + s
   n = n // base
print(s)
