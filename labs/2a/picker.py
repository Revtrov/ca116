#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
print(b * (c % 2) + a * (1 - (c % 2)))
