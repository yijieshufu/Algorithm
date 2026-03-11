import os
import sys
it = iter(sys.stdin.read().split())
a = float(next(it))
b = float(next(it))
print(int(a**(1/b)*1000))
