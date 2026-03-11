import os
import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a = [int(next(it)) for _ in range(n)]
neg = sorted([-x for x in a if x<0])
pos = sorted([x for x in a if x>=0])
ans = 0 
j = len(pos)
for i in range(len(neg)+1):
  L = neg[i-1] if i>0 else 0 
  if L>m:
    break
  while j >0:
    R = pos[j-1]
    dist = min(2*L+R, 2*R+L)
    if dist<=m:
      break
    j-=1
  ans =max(ans,i+j)
print(ans)
