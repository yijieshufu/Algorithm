import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
res = 0
for _ in range(n):
  a = int(next(it))
  if a>0 and (a&(a-1))==0:
    res+=1
print(res)
