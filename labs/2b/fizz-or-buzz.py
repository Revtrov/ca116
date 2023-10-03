#!/usr/bin/env python3

s = input()
n = int(s)
div3 = (n % 3)
div5 = (n % 5)
div15 = (n % 15)
if not div5 or not div3:
   s = ((1 - div3) * "fizz") + ((1 - div15) * "-") + ((1 - div5) * "buzz")
print(s)
