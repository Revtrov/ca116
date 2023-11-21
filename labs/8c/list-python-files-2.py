#!/usr/bin/env python3

import os

dir = os.listdir(".")

i = 0
while i < len(dir):
  if dir[i][len(dir[i]) - 3:len(dir[i])] == ".py":
    with open(dir[i], "r") as f:
      if f.read() != "":
        print(dir[i])
  i += 1
