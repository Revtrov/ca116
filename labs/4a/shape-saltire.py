#!/usr/bin/env python3

#!/usr/bin/env python3

n = int(input())
i = 0
j = 0
flip = 0
mid = n // 2
pivot = (mid + 1)
while i < n:
   double = "*"
   diff = 2 * (j + 1)
   iFlip = 1 - flip
   outSpace = " " * (((j % pivot) * iFlip) + (((mid - j - 1) % pivot) * flip))
   inSpace = " " * (((n - diff) * iFlip) + ((diff - 1) * flip))
   if i == mid:
      double = ""
   print(outSpace + "*" + inSpace + double)
   if j < mid:
      j += 1
   else:
      j = 0
      flip = 1
   i += 1
