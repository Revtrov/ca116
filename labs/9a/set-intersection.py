#!/usr/bin/env python3

words = {}

with open("b.txt", "r") as f:
  lines = f.readlines()
  i = 0
  while i < len(lines):
    words[lines[i].strip()] = True
    i += 1

with open("a.txt", "r") as s:
  lines = s.readlines()
  i = 0
  while i < len(lines):
    if lines[i].strip() in words and words[lines[i].strip()]:
      words[lines[i].strip()] = False
      print(lines[i].strip())
    i += 1
