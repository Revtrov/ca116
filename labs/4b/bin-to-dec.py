#!/usr/bin/env python3

binary = input()
decimal = 0
i = 0
while i < len(binary):
   decimal += (2 ** i) * int(binary[len(binary) - i - 1])
   i += 1
print(decimal)
