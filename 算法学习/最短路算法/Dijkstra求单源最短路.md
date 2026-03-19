# Dijkstra求最短路
给定一个包含 $n$ 个点、$m$ 条边的**带权有向图**（存在自环和重边），计算从 **1 号点**到 **$n$ 号点**的最短路径长度。若不可达则输出 -1。  
**数据范围**：$n \le 500$，$m \le 10^5$，边权 $c \le 10^4$。
# 分析
**Dijkstra 算法（堆优化版）**
- **原因**：题目要求 **单源最短路**，使用迪杰斯特拉算法 配合 **优先队列（堆）**
### 解题思路
1. **图的存储**：采用邻接表
2. **初始化距离数组**：设置 `dist` 数组，除起点 `dist[1] = 0` 外，其余初始化为**无穷大**。
3. **采用小根堆**：
    - 将 `(0, 1)` 放入小根堆，（距离，节点）
    - 每次弹出堆顶距离最小的节点 `u`。
    - 遍历 `u` 的所有邻接点 `v`，若 `dist[u] + w < dist[v]`，则更新 `dist[v]` 并将其入堆。
4. **安全判断**：最后检查 `dist[n]` 是否仍为无穷大。
## 代码
```python
import sys,heapq
# 数据读入
it = iter(sys.stdin.read().split())
n,m = int(next(it)),int(next(it))
# 邻接表
g = [[] for _ in range(n+1)] # 记录节点的边
for _ in range(m):
  u,v,w=int(next(it)),int(next(it)),int(next(it))
  g[u].append((v,w))

dist=[float("inf")]*(n+1) # 到n的距离

dist[1] = 0
pq = [(0,1)] #(距离,节点)
while pq:
  d,u = heapq.heappop(pq)
  if d > dist[u]: continue
  for v,w in g[u]:
    if dist[u]+w<dist[v]:
      dist[v]=dist[u]+w
      heapq.heappush(pq,(dist[v],v))
print(dist[n] if dist[n]!=float("inf") else -1)
```
