import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a = [int(x) for x in it]
a.sort()
ans = float('inf') # 极大值
for i in range(n-m+1):
  diff = a[i+m-1]**2 - a[i]**2
  if diff< ans:
    ans = diff
print(ans)
