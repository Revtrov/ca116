#!/usr/bin/env python3

reversed = 0
i = 0
while i < 10:
   reversed += int(input()) * (10 ** (10 - 1 - i))
   i += 1
i = 0
while i < 10:
   power = 10 ** i
   print(((reversed % (10 ** (i + 1)) - (reversed % power))) // power)
   i += 1
