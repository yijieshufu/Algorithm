import os
import sys
from collections import Counter
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
c = Counter(a)
ans =0
now = 1
for i in range(1,n): # i代表的是数字
  if c[i]>0:
    now*=c[i] #关键点
    ans+=now
  else:
    break
print(ans)
