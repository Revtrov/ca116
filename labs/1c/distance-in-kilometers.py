#!/usr/bin/env python3

dist = int(input())
km = dist // 1000
up = ((dist - (km * 1000)) // 500)
print(km + up)
