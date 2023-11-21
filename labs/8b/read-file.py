#!/usr/bin/env python3

with open("input.txt", "r") as f:
   line = f.readline()
   while line != "":
      print(line[0:len(line) - 1])
      line = f.readline()
