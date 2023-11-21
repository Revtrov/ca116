#!/usr/bin/env python3

import sys

with sys.stdin as f:
   line = f.readline()
   while line != "":
      print(line.split("/")[-1].strip())
      line = f.readline()
