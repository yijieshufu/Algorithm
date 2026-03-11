import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [0]+[int(next(it)) for _ in range(n)]
vis = [False]*(n+1)
ans = 0 
for i in range(1,n+1):
  if not vis[i]:
    curr= i 
    cnt = 0
    while not vis[curr]:
      vis[curr] = True
      curr = a[curr]
      cnt+=1 # 当前错误的书籍数量 环的大小
    if cnt>1:
      ans+=(cnt-1) # 环-1也就是 交换多少次恢复到正确的顺序
print(ans)
