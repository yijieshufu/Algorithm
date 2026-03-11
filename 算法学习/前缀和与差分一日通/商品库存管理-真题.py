import os
import sys
it=iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
ops =[]
diff= [0]*(n+2)
for _ in range(m):
  L = int(next(it));R = int(next(it))
  ops.append((L, R))
  diff[L]+=1
  diff[R+1]-=1
count = [0]*(n+1)
base_zeros = 0
curr = 0
for i in range(1,n+1):
  curr += diff[i]
  count[i] = curr
  if count[i]==0:
    base_zeros+=1
pre1= [0]*(n+1)
for i in range(1,n+1):
  pre1[i] = pre1[i-1]+(1 if count[i]==1 else 0)
ans = []
for l,r in ops:
  res= base_zeros+ (pre1[r]-pre1[l-1])
  ans.append(str(res))
sys.stdout.write('\n'.join(ans)+'\n')
