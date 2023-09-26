#!/usr/bin/env python3

month = int(input()) - 1
dayNum = int(input()) - 1
print((((((month) * 30) + dayNum)) % 7) + 1)
