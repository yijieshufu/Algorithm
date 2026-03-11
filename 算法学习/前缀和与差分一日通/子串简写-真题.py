import os
import sys
it = iter(sys.stdin.read().split())
# 2. 获取参数
K = int(next(it))
S = next(it)
c1 = next(it)
c2 = next(it)
n = len(S)
ans = 0
cnt_c1= 0 
for j in range(n):
  i = j-K+1
  if i >=0 and S[i]==c1:
    cnt_c1+=1
  if S[j]==c2:
    ans+=cnt_c1
print(ans)
