#!/usr/bin/env python3

import sys
args = sys.argv[1:]
j = 0
nums = []
while j < len(args):
   aFile = args[j]
   aList = []
   with open(aFile, 'r') as a:
      aList = a.readlines()
      i = 0
      subTot = 0
      while i < len(aList):
         subList = aList[i].split(" ")
         iter = 0
         while iter < len(subList):
            subTot += int(subList[iter])
            iter += 1
         i += 1
   nums = nums + [subTot]
   j += 1
total = 0
i = 0
while i < len(nums):
   total += int(nums[i])
   i += 1
print(total)
