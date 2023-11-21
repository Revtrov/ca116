#!/usr/bin/env python3

import sys

file_name = "irish-dobs.txt"
file_to = "american-dobs.txt"
records = []
with open(file_to, "w") as f:
   with open(file_name, "r") as f2:
      line = f2.readline()
      while line != "":
         records.append(line)
         line = f2.readline()
      i = 0
      while i < len(records):
         deviders = records[i].split("/")
         day = deviders[0]
         month = deviders[1]
         end = deviders[-1]
         records[i] = month + "/" + day + "/" + end
         i += 1
      f.writelines(records)
