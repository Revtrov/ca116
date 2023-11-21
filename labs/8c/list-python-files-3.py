#!/usr/bin/env python3

import os

dir = os.listdir(".")

i = 0
while i < len(dir):
  with open(dir[i], "r") as f:
    lines = f.readlines()
    if len(lines) >= 1 and lines[0] != "":
      if dir[i][len(dir[i]) - 3:len(dir[i])] == ".py":
        print(dir[i])
      if lines[0] == "#!/usr/bin/env python3\n":
        print(dir[i])
  i += 1
