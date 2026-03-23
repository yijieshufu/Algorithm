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
# 出差-真题 （变体：边权的转化）
**【材料】 (Materials)**
- **城市与道路**：$N$ 个点（城市），$M$ 条**带权无向边**（道路耗时）。
- **隔离时间**：每个城市 $i$ 都有一个固定的点权 $C_i$（隔离时间）。
- **规模**：$N=1000$，$M=10000$。这个规模暗示 $O(M \log N)$ 的 Dijkstra 是完美选择。  
**【条件】 (Constraints)**
- **隔离规则**：到达一个城市后，必须先隔离才能离开前往下一站。
- **特殊豁免**：
    1. **起点（城市 1）**：离开时不需要隔离。
    2. **终点（城市 $N$）**：到达后不需要隔离。
- **双向通行**：所有道路都是**双向的**。  
**【目的】 (Objective)**
- 计算从城市 1 到达城市 $N$ 的**最小总耗时**。
## 分析
#### **1. 遇到“点权（隔离时间）” $\rightarrow$ 想到“边权转化”**
- **分析**：标准的 Dijkstra 只能处理边权。这道题的耗时由“路程时间”+“隔离时间”组成。
- **逻辑**：我们可以把隔离时间平摊到进入该城市的“路”上。
    - 假设有一条路连接 $u$ 和 $v$，耗时为 $w$。
    - 如果你从 $u$ 走到 $v$，你实际付出的代价是：**路程耗时 $w$ + 在城市 $v$ 的隔离时间 $C_v$**。
- **特殊处理**：由于到达城市 $N$ 不用隔离，所以如果这条路的终点是 $N$，代价仅为 $w$。
#### **2. 遇到 $N=1000, M=10000$ $\rightarrow$ 想到“堆优化 Dijkstra”**
- **分析**：这是一个典型的单源最短路问题。
- **决策**：使用 `heapq` 维护一个优先级队列，每次取出当前距离最小的点。
## 代码

```python
import sys
import heapq
# 读入数据
it =iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
# 隔离代价
c = [int(next(it)) for _ in range(n)]
# 邻接表
g = [[] for _ in range(n+1)]
# 构建图的代价
for _ in range(m):
  u,v,w= int(next(it)),int(next(it)),int(next(it))
  cost_u_to_v = w + (c[v-1] if v!= n else 0)
  cost_v_to_u = w + (c[u-1] if u!= n else 0)
  g[u].append((v,cost_u_to_v))
  g[v].append((u,cost_v_to_u))
# 单源最短路径算法
dist = [float("inf")]*(n+1)
dist[1]=0
pq= [(0,1)] #(距离，节点)
while pq:
  d,u = heapq.heappop(pq)
  if d > dist[u]: continue
  for v,w in g[u]:
    if dist[u]+w<dist[v]:
      dist[v] = dist[u]+w
      heapq.heappush(pq,(dist[v],v))
print(dist[n])
```
# 染色时间-真题
**【原料】 (Materials)**
- **空间**：一个 $n \times m$ 的网格棋盘。
- **属性**：每个格子 $(i, j)$ 有一个独立的染色耗时 $t_{ij}$。
- **起点**：在时刻 $0$ 触发第一行第一列 $(1, 1)$。
- **规模**：$n, m \le 500$。这意味着总格子数 $N = n \times m \le 250,000$。  
**【条件】 (Constraints)**
- **触发机制**：一个格子被触发后，需经过 $t_{ij}$ 秒才会变色。
- **扩散机制**：变色瞬间，**立即**向上下左右四个邻居发起染色触发。
- **唯一性**：每个格子只会被触发一次（即第一次到达该格子的信号有效）。
- **并行性**：所有被触发的格子是**同时进行**染色计时的。  
**【目的】 (Objective)**
- 计算**整个棋盘完成染色**的时间。这意味着我们需要找到所有格子中，**最晚变色**的那个格子的变色时刻。
## 分析
#### **1. 遇到“时间成本”与“邻居扩散” $\rightarrow$ 想到“最短路算法”**
- **分析**：从起点出发，信号传到邻居的**代价**就是邻居自身的**染色时间**。
- **逻辑**：将每个格子看作一个节点。如果从格子 $A$ 走到格子 $B$，边权就是 $B$ 的染色时间 $t_B$。
- **结论**：求起点 $(1, 1)$ 到所有格子的“最短路径”，这个路径长度就是该格子完成染色的最早时刻。
#### **2. 遇到“边权非负”且“节点较多” $\rightarrow$ 想到“堆优化 Dijkstra”**
- **分析**：染色时间 $t_{ij}$ 都是正整数（无负权），且 $N \times M$ 规模在 25 万级别。
- **决策**：堆优化 Dijkstra 的复杂度为 $O(E \log V)$，在此处约为 $O(4NM \log NM)$，完全能过。
#### **3. 遇到“整个棋盘完成” $\rightarrow$ 想到“求最大值”**
- **分析**：Dijkstra 算出的是每个格子变色的“最早时刻”。
- **逻辑**：棋盘全部染完，意味着最后一个格子也变色了。
- **决策**：结果 = $\max(\text{所有格子的最短路时间})$。
## 代码
```python
# 读入数据
it = iter(sys.stdin.read().split())
n,m =int(next(it)),int(next(it))
t = [[int(next(it)) for _ in range(m)] for _ in range(n)]
# Dijkstra 初始化
dist = [[float("inf")]*(m) for _ in range(n)]
# 起点 (0,0) 开始染色，完成时间是它自己的 t[0][0]
dist[0][0] = t[0][0]
pq = [(dist[0][0],0,0)] # (距离，节点)
ans = 0
while pq :
  d,r,c = heapq.heappop(pq)
  if d> dist[r][c]: continue
  ans = max(ans,d)
  for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
    nr,nc = r+dr,c+dc
    if 0<=nr<n and 0<=nc<m:
      new_d = d + t[nr][nc]
      if new_d < dist[nr][nc]:
        dist[nr][nc] = new_d
        heapq.heappush(pq,(new_d,nr,nc))
print(ans)
```
