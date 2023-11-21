#!/usr/bin/env python3

words = {}

with open("b.txt", "r") as f:
  lines = f.readlines()
  i = 0
  while i < len(lines):
    if lines[i].strip() not in words:
      words[lines[i].strip()] = True
      print(lines[i].strip())
    i += 1

with open("a.txt", "r") as s:
  lines = s.readlines()
  i = 0
  while i < len(lines):
    if lines[i].strip() not in words:
      words[lines[i].strip()] = False
      print(lines[i].strip())
    i += 1
