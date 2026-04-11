# Dijkstra求最短路
给定一个 `n` 个点、`m` 条边的带权有向图，可能有**重边和自环**。  
求从 `1` 号点到 `n` 号点的最短路长度；如果到不了，输出 `-1`。  
数据范围：`n <= 500`，`m <= 1e5`，边权为正。
# 分析
用 Dijkstra + 小根堆。

- 因为边权 `c >= 1`，没有负权，Dijkstra 适用。
- `d[i]`：当前已知 `1` 到 `i` 的最短距离。
- 每次从堆里取距离最小的点去“扩展”它的出边，尝试更新相邻点（松弛）。

## 代码
```python
import sys
import heapq
it = iter(sys.stdin.read().split())
n = int(next(it));m = int(next(it))

g = [[] for _ in range(n+1)] # 邻接表 有向边
for _ in range(m):
  a = int(next(it));b = int(next(it));c = int(next(it))
  g[a].append((b,c))

inf = 10**30
d = [inf] *(n+1)
d[1] = 0
q= [(0,1)] # (距离，节点)
while q:
  x,a = heapq.heappop(q)
  if x!= d[a]:
    continue
  for b,c in g[a]:
    f = x + c # 新的距离
    if f < d[b]: # 找最短距离
      d[b] = f
      heapq.heappush(q,(f,b))

ans = d[n]
print(-1 if ans ==inf else ans)
```

