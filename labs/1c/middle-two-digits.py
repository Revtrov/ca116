#!/usr/bin/env python3

num = int(input())
thou = num - ((num // 10000) * 10000)
print((num - ((num // 10000) * 10000)) // 100)
