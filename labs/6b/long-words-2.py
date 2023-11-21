#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
done = 0
while i < len(a) and not done:
   if len(a[i]) >= 6:
      print(a[i])
      done = 1
   i += 1
