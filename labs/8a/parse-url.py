#!/usr/bin/env python3

import sys
url = sys.argv[1:][0]
outputs = ["scheme", "host", "port", "path", "query-string", "fragment-id"]
outputvars = []
outputvars.append(url.split(":")[0])
host = url.split("//")[1].split("/")
outputvars.append(host[0].split(":")[0])
outputvars.append(url.split(":")[-1].split("/")[0])
outputvars.append("/" + "/".join(host[1:]).split("#")[0].split("?")[0])
if len(url.split("?")) > 1:
   outputvars.append(url.split("?")[-1].split("#")[0])
else:
   outputvars.append("")
outputvars.append(url.split("#")[-1])
i = 0
while i < len(outputvars):
   if outputvars[i] != "" and outputvars[i] != url:
      print(outputs[i] + ": " + outputvars[i])
   i += 1
