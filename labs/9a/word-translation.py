#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
map = {}
with open("translation.txt") as f:
  lines = f.readlines()
  i = 0
  while i < len(lines):
    map[lines[i].strip().split(" ")[0]] = lines[i].strip().split(" ")[1]
    i += 1
i = 0
while i < len(words):
  if words[i].strip() in map:
    print(map[words[i].strip()])
  i += 1
