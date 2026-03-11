import os
import sys
it = iter(sys.stdin.read().split())
L = int(next(it))
if L < 2:print(0)
else:
  # 计算约数的个数
  d = [0]*(L+1)
  for i in range(1,L+1):
    for j in range(i,L+1,i):
      d[j]+=1
  # 计算约数前缀的个数
  G = [0]*(L+1)
  for i in range(1,L+1):
    G[i]=G[i-1]+d[i]
  ans = 0
  for s in range(1,L):
    ans += d[s] * G[L - s]
  print(ans)
