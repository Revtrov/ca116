#!/usr/bin/env python3

wordsA = {}
disjoint = True
with open("b.txt", "r") as f:
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i] != "\n":
            wordsA["n" + lines[i].strip()] = True
        i += 1
with open("a.txt", "r") as s:
    lines = s.readlines()
    i = 0
    while i < len(lines):
        if lines[i] != "\n":
            if "n" + lines[i].strip() in wordsA and disjoint:
                disjoint = False
        i += 1
if disjoint:
    print("disjoint")
else:
    print("intersecting")
