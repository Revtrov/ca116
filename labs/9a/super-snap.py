#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
cards = {
}
snapped = False
i = 0
while i < len(words):
  if words[i].strip() in cards and not snapped:
    print("snap: " + words[i].strip())
    snapped = True
  cards[words[i].strip()] = True
  i += 1
