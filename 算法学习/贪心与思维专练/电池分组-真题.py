import os
import sys
it = iter(sys.stdin.read().split())
t = int(next(it))
for _ in range(t):
  n = int(next(it))
  res = 0
  for _ in range(n):
    res ^= int(next(it))
  if res == 0:
    print("YES")
  else:print("NO")
