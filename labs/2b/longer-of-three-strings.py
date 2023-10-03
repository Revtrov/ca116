#!/usr/bin/env python3

s1 = input()
s2 = input()
s3 = input()
toPrint = s3
s1Len = len(s1)
s2Len = len(s2)
s3Len = len(s3)
if s1Len > s2Len and s1Len > s3Len:
   toPrint = s1
elif s2Len > s1Len and s2Len > s3Len:
   toPrint = s2
print(toPrint)
