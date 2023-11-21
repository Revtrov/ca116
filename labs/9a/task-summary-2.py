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
otherNames = []
i = 0
while i < len(words):
  fileName = ".".join(words[i].split(".")[0:len(words[i].split(".")) - 1])
  status = words[i].split(".")[-1].strip()
  if (fileName in completed) and completed[fileName] == "correct":
    names.append(fileName)
    completed[fileName] = "beans"
  else:
    otherNames.append(fileName)
  i += 1
namesDict = {}
i = 0
while i < len(names):
  if not(names[i].split("/")[0] in namesDict):
    namesDict[names[i].split("/")[0]] = 1
  else:
    namesDict[names[i].split("/")[0]] += 1
  i += 1
i = 0
while i < len(otherNames):
  if not(otherNames[i].split("/")[0] in namesDict):
    namesDict[otherNames[i].split("/")[0]] = 0
  i += 1
for key in namesDict:
  print(key, namesDict[key])
