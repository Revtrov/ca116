#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
germ = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "vier",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn"
}
i = 0
while i < len(words):
  if words[i].strip() in germ:
    print(germ[words[i].strip()])
  i += 1
