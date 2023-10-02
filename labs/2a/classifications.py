#!/usr/bin/env python3

mark = int(input())
print(f"first: {mark >= 70}")
print(f"second: {mark >= 50 and mark <= 69}")
print(f"third: {mark >= 40 and mark <= 49}")
print(f"fail: {mark < 40}")
