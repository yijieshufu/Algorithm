import sys
import heapq
# 读入数据
it = iter(sys.stdin.read().split())
n,m =int(next(it)),int(next(it))
t = []
for _ in range(n):
    t.append([int(next(it)) for _ in range(m)])
# Dijkstra 初始化
dist = [[float("inf")]*(m) for _ in range(n)]
dist[0][0]=t[0][0]
pq = [(dist[0][0],0,0)]
ans = 0
# 单源最短路径
while pq:
    d,r,c = heapq.heappop(pq)
    if d>dist[r][c]:continue
    ans = max(ans,d)
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<n and 0<=nc<m:
            new_d = d + t[nr][nc]
            if new_d<dist[nr][nc]:
                dist[nr][nc] = new_d
                heapq.heappush(pq,(new_d,nr,nc))
print(ans)