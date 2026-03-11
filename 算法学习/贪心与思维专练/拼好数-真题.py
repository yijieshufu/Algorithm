import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
c= [0] * 7
ans = 0 
for _ in range(n):
  s = next(it)
  cnt = s.count('6')
  if cnt>=6: # 独立成组
    ans+=1
  else:
    c[cnt]+=1
for i in [5, 4, 3]: # 大数找小数
  for j in range(1, 6): #
    if i + j >= 6:
      if i == j:
        num = c[i]//2
        ans+=num
        c[i]%=2
      else:
        num = min(c[i],c[j])
        ans+=num
        c[i]-=num
        c[j]-=num
v = c[2]//3  # 2 2 2 
ans +=v
c[2]%=3
v = min(c[3],c[2],c[1])  #3 2 1
ans +=v
c[3]-=v
c[2]-=v
c[1]-=v
v = min(c[4],c[1]//2) # 4 1 1 
ans +=v
c[4]-=v
c[1]-=2*v
print(ans)
