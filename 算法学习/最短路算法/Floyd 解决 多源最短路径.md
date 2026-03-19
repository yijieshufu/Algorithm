# 蓝桥公园
- **基础组件**：一个包含 $N$ 个景点和 $M$ 条道路的**带权无向图**。
- **核心输入**：$M$ 条双向道路的起点 $u$、终点 $v$ 及距离 $w$；以及 $Q$ 组查询计划（起点 $st$ 到终点 $ed$）。
- **数值规模**：$N$ 最高 400，$Q$ 最高 1000，边权 $w$ 可达 $10^9$。  
算出图中**任意两点**之间的最短距离。
# 分析
#### **1. 遇到 $N=400$ 且查询多 求全源 $\rightarrow$ 想到 Floyd-Warshall**
- **分析**：Dijkstra 适合单源，而 Floyd 适合**全源**。
- **逻辑**： 

| **算法**             | **单源复杂度**     | **全源复杂度 (跑 N 次)**     | **适用场景**                                    |
| ------------------ | ------------- | --------------------- | ------------------------------------------- |
| **Dijkstra (堆优化)** | $O(M \log N)$ | $O(N \cdot M \log N)$ | 稀疏图 ($M \approx N$)，点数多但边少                  |
| **Floyd-Warshall** | —             | **$O(N^3)$**          | **稠密图** ($M \approx N^2$)，点数少 ($N \le 500$) |
- **结论**：Floyd 直接求出 $f[i][j]$，代表i到j的最短距离

**Floyd 算法**：  
**状态定义**：$f[k][i][j]$ 表示“只允许经过前 $k$ 个点作为中转点”时，$i$ 到 $j$ 的最短路。  
**转移方程**：  
$$f[k][i][j] = \min(f[k-1][i][j], f[k-1][i][k] + f[k-1][k][j])$$

**通用骨架**：
```python
# --- 1. 初始化 (Preparation) ---
inf = float("inf")
dist = [[inf] * (n + 1) for _ in range(n + 1)]

# 每一个点到自己的距离是 0
for i in range(1, n + 1):
    dist[i][i] = 0

# --- 2. 存入边 (Edge Storage) ---
# 注意：无向图对称存边，且保留重边中的最小值
for _ in range(m):
    u, v, w = map(int, next(it))
    if w < dist[u][v]:
        dist[u][v] = dist[v][u] = w

# --- 3. 核心三层循环 (DP Core) ---
# k: 中转点, i: 起点, j: 终点
for k in range(1, n + 1):
    for i in range(1, n + 1):
        # 优化：如果起点连不上中转点，直接跳过内层循环
        if dist[i][k] == inf: continue
        for j in range(1, n + 1):
            # 状态转移方程: dist[i][j] = min(直接走, 经过 k 绕路走)
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# --- 4. 判定与输出 (Output) ---
# ans = dist[st][ed]
# print(ans if ans != inf else -1)
```
## 代码

```python
import sys
# 读入数据
it =iter(sys.stdin.read().split())
n = int(next(it)) # n
m = int(next(it)) # m条边
q = int(next(it)) # q查询
# 初始化邻接矩阵 构建图
inf = float("inf")
f = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    f[i][i]=0
# 存入边
for _ in range(m):
    u,v,w = map(int,next(it))
    if w < f[u][v]: 
        f[u][v]=f[v][u]=w
# Floyd 算法
for k in range(1,n+1):
    fk = f[k]
    for i in range(1,n+1):
        fi = f[i]
        if fi[k]==inf :continue
        fik = fi[k]
        for j in range(1,n+1):
            if fik+fk[j]<fi[j]:
                fi[j]=fik+fk[j]
# 查询
for _ in range(q):
    st , ed = int(next(it)),int(next(it))
    ans = f[st][ed]
    print(ans if ans!= inf else -1)
```
