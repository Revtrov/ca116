#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
completed = {}
i = 0
while i < len(words):
  fileName = ".".join(words[i].split(".")[0:len(words[i].split(".")) - 1])
  if words[i].split(".")[-1] == "correct" and completed[fileName] is True:
    completed[fileName] = False
  print(completed)
  if not (fileName in completed):
    completed[fileName] = True
  if (fileName in completed) and not completed[fileName]:
    print(fileName)
  i += 1