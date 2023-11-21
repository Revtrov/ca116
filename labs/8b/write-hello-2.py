#!/usr/bin/env python3

import sys

filename = sys.argv[1:][0]
with open(filename, "w") as f:
   f.write("Hello world.\n")
