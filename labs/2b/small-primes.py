#!/usr/bin/env python3

n = int(input())
prime = "prime"
if n == 1:
   prime = "not prime"
elif not (n % 2) and n != 2:
   prime = "not prime"
elif not (n % 3) and n != 3:
   prime = "not prime"
elif not (n % 5) and n != 5:
   prime = "not prime"
elif not (n % 7) and n != 7:
   prime = "not prime"
print(prime)
