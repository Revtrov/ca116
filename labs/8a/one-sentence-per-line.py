#!/usr/bin/env python3

s = input()
sList = []
while s != "end":
   sList.append(s)
   s = input()
paragraph = " ".join(sList)
sentences = paragraph.split(".")
i = 0
while i < len(sentences):
   sentences[i] += "."
   sentences[i] = sentences[i].strip()
   sentences[i] = " ".join(sentences[i].split())
   if sentences[i] != ".":
      print(sentences[i])
   i += 1
