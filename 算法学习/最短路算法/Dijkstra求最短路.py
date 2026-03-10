import sys,heapq
# 数据读入
it = iter(sys.stdin.read().split())
n,m = int(next(it)),int(next(it))
# 创建图 读入数据 
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w=int(next(it)),int(next(it)),int(next(it))
    g[u].append((v,w))
# 创建距离地图
dist = [float('inf')]*(n+1)
dist[1]=0
pq = [(0,1)] # 
while pq:
    d,u = heapq.heappop(pq)
    if d>dist[u]:continue
    for v,w in g[u]:
        if dist[u]+w< dist[v]:
            dist[v] = dist[u]+w
            heapq.heappush(pq,(dist[v],v))
print(dist[n] if dist[n]!=float("inf") else -1)
