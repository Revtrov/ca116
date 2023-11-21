#!/usr/bin/env python3

decimal = int(input())
binaryF = ""
binaryB = ""
while decimal != 0:
   binaryB += str((decimal % 2))
   decimal = decimal // 2
i = 0
while i < len(binaryB):
   binaryF += binaryB[len(binaryB) - i - 1]
   i += 1
print(binaryF)
