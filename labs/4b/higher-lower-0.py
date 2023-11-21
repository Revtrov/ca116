#!/usr/bin/env python3

n = int(input())
m = 1
while n != 0:
   m = int(input())
   if m != 0:
      if n < m:
         print("higher")
      elif n > m:
         print("lower")
      else:
         print("equal")
   n = m
