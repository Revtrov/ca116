#!/usr/bin/env python3

#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
   s = "mont"

done = 0
i = 0
while i < len(a) and not done:
   if a[i][0:len(s)] == s:
      print(a[i])
      done = 1
   i += 1
