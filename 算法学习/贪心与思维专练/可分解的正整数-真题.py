import os
import sys
it = iter(sys.stdin.read().split())
ans = 0
N = int(next(it))
for _ in range(N):
  A = int(next(it))
  if A>1:
    ans+=1
print(ans)
