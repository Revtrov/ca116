#!/usr/bin/env python3

num = int(input())
digit = num % 10
ten = (num % 100) // 10
hundred = (num % 1000) // 100
print(hundred)
print(ten)
print(digit)
