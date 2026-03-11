
# 该代码 内存有些 超时
import sys
import heapq
it = iter(sys.stdin.read().split())
n,m= int(next(it)),int(next(it))
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w= int(next(it)),int(next(it)),int(next(it))
    g[u].append((v,w));g[v].append((u,w))
# prim
vis = [False]*(n+1)
pq = [(0,1)]  # (耗时, 传送点编号)
ans = 0
cnt = 0
while pq and cnt <n:
    w,u=heapq.heappop(pq) # 保证了 弹出的 是最小
    if vis[u]:continue
    vis[u]=True
    ans+=w
    cnt+=1
    for v,weight in g[u]:
        if not vis[v]:
            heapq.heappush(pq,(weight,v))
print(ans if cnt ==n else -1)
