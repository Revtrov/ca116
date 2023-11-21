#!/usr/bin/env python3

import os

with open("start.txt", "r") as f:
  contents = f.read().strip()
  if os.path.isdir(contents) or os.path.isfile(contents):
    files = os.listdir()
    i = 0
    while i <= len(files) and files[i] != contents:
      i += 1
    if i >=  len(files):
      print(contents)
    else:
      with open(files[i], "r") as f2:
        contentsB = f2.read().strip()
