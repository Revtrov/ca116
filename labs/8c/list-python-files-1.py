#!/usr/bin/env python3

import os

dir = os.listdir(".")

i = 0
while i < len(dir):
  if dir[i][len(dir[i]) - 3:len(dir[i])] == ".py":
    print(dir[i])
  i += 1
