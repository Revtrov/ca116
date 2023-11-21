#!/usr/bin/env python3

import sys
args = sys.argv[1:]
with open(args[0], "w") as f:
   f.write("Hello world.\n")
