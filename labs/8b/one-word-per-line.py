#!/usr/bin/env python3

import sys

with sys.stdin as f:
   line = f.readlines()
   print("\n".join(" ".join(line).replace(" ", "\n").split()))
