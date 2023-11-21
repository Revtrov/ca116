#!/usr/bin/env python3

import sys
n = int(sys.argv[1:][0])
i = 0
flip = 1
while i < n:
   mid = n // 2
   inverse = n - i
   if inverse == mid:
      flip = -1
   spaces = (inverse - mid - 1) * flip
   asters = n - (2 * spaces)
   print(spaces * " " + asters * "*")
   i += 1
