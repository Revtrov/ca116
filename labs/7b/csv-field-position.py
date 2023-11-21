#!/usr/bin/env python3

import sys
n = sys.argv[1]
sList = [input()]
i = 0
while i < len(sList[0]) and sList[0][i:len(n)] != n:
   i += 1
print(i)
