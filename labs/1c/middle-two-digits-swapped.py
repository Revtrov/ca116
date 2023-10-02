#!/usr/bin/env python3

num = int(input())
thou = num - ((num // 10000) * 10000)
print((thou // 1000) + ((thou // 100) - ((thou // 1000) * 10)) * 10)
