# 星际旅行-真题
**【材料】 (Materials)**
- **空间数据**：$N$ 个星球（节点），$M$ 条传送门（边权均为 $1$ 的无向边）。
- **任务数据**：$Q$ 个盲盒，每个盲盒包含起点 $x_i$ 和步数限制 $y_i$。
- **数据规模**：$N=1000$，$Q=50000$。这意味着 $O(N^2)$ 的空间是可以接受的，但 $O(Q \cdot N)$ 的暴力枚举必死。  
**【条件】 (Constraints)**
- **无权图最短路**：步数即距离。在边权为 $1$ 的图中，距离计算首选 **BFS**。
- **可达性定义**：距离起点 $dist \le y_i$ 的所有点均可计入。
- **数学定义**：期望值 $\text{ans} = \frac{\sum \text{每个方案可达数}}{Q}$。
- **输出限制**：保留两位小数。  
**【目的】 (Objective)**
- 快速统计每个起点在不同步数限制下的可达星球总数，并计算所有查询的平均值。
## 分析
#### **第一步：遇到“步数限制 $y$ 内的所有点” $\rightarrow$ 想到“BFS 距离层级”**
- **分析**：因为边权恒为 $1$，BFS 是一层一层向外扩散的。
- **逻辑**：第 $d$ 层搜到的点，距离起点的最短距离就是 $d$。
- **决策**：对每个点跑一遍 BFS，统计距离为 $0, 1, 2 \dots d$ 的点各有多少个。
#### **第二步：遇到“$Q$ 巨大且 $N$ 较小” $\rightarrow$ 想到“前缀和预处理”**
- **分析**：即便有了距离分布，如果每次查询 $(x, y)$ 都去求和 $\sum_{d=0}^{y} \text{count}[x][d]$，依然太慢。
- **逻辑**：利用**前缀和**。定义 $f[x][d]$ 为星球 $x$ 在距离 $d$ 以内（包含 $d$）能到达的星球总数。
- **决策**：
    1. 统计每个距离的点数：`f[x][dist] += 1`。
    2. 累加前缀和：`f[x][d] = f[x][d] + f[x][d-1]`。
    3. 这样查询 $(x, y)$ 时，只需 $O(1)$ 访问 `f[x][y]`。
#### **第三步：遇到“$y$ 可能很大” $\rightarrow$ 想到“边界保护”**
- **分析**：$y$ 可能给到 $10^9$，但星球最多只有 $N$ 个，最远距离不会超过 $N$。
- **决策**：查询时使用 `min(y, n)`，防止数组越界。
## 代码

```python
import sys

# 1. 变量 (材料读入)
it = iter(sys.stdin.read().split())
n, m, q = int(next(it)), int(next(it)), int(next(it))
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = int(next(it)), int(next(it))
    g[u].append(v)
    g[v].append(u)

# 2. 边界 (全源 BFS 与距离分布统计)
# f[i][d] 最初表示：i 走 d 步恰好到达的星球数
f = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist = [-1] * (n + 1)
    dist[i] = 0
    que = [i]
    # Python 极简 BFS 技巧：直接遍历增长的列表
    for u in que:
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                que.append(v)
    
    # 3. 操作 (统计分布并转换成前缀和)
    for d in dist:
        if d != -1:
            f[i][d] += 1
            
    # 计算距离 <= d 的累积星球数
    for d in range(1, n + 1):
        f[i][d] += f[i][d-1]

# 4. 答案 (离线查询累加)
total_count = 0
for _ in range(q):
    x, y = int(next(it)), int(next(it))
    # 限制 y 的范围，防止索引溢出
    total_count += f[x][min(n, y)]

print(f"{total_count / q:.2f}")
```
