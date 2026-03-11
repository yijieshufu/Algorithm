import sys
import heapq
# 读入数据
it =iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
# 隔离代价
c_list =[0]+[int(next(it)) for _ in range(n)]
c_list[n]=0 
# 构建图
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,w = int(next(it)),int(next(it)),int(next(it))
    g[u].append((v,w+c_list[v]));g[v].append((u,w+c_list[u]))
# Dijkstra 核心逻辑
dist = [float("inf")] * (n+1)
dist[1]= 0 
pq = [(0,1)]
while pq:
    d,u =heapq.heappop(pq)
    if d >dist[u]:continue
    for v,weight in g[u]:
        if dist[u]+weight<dist[v]:
            dist[v]=dist[u]+weight
            heapq.heappush(pq,(dist[v],v))
print(dist[n])