#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
completed = {}
i = 0
while i < len(words):
  fileName = ".".join(words[i].split(".")[0:len(words[i].split(".")) - 1])
  status = words[i].split(".")[-1].strip()
  completed[fileName] = status
  i += 1
names = []
namesDict = {}
i = 0
while i < len(words):
  fileName = ".".join(words[i].split(".")[0:len(words[i].split(".")) - 1])
  status = words[i].split(".")[-1].strip()
  if fileName in completed and completed[fileName] == "correct":
    names.append(fileName)
  i += 1
i = 0
while i < len(names):
  if not(names[i] in namesDict):
    namesDict[names[i]] = True
    print(names[i])
  i += 1
