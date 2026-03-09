
基础模型通常定义 $dp[i][j]$ 为到达 $(i, j)$ 的方案数，转移方程为：

$$dp[i][j] = dp[i-1][j] + dp[i][j-1]$$

# 基础模型：网格路径计数

这是最纯粹的 DP 形式。假设没有转向限制，也没有障碍物，从 $(1, 1)$ 到 $(n, m)$ 只能向下或向右。

```Python
import sys

# 1. 输入处理
d = sys.stdin.read().split()
if not d: exit()
n = int(d[0])
m = int(d[1])

# 2. 初始化 DP 数组
dp = [[0] * m for _ in range(n)]

# 3. 起点初始化
dp[0][0] = 1

# 4. 填表 (使用 range(n) 风格)
for i in range(n):
    for j in range(m):
        # 跳过起点
        if i == 0 and j == 0:
            continue
        
        # 状态转移：方案数 = 来自上方 + 来自左方
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]

# 5. 输出结果
print(dp[n-1][m-1])
```

# 变体

## k-转弯路径限制计数
题目：[[动态规划的基础/地图]]

**核心约束**：
	只能向右或向下移动。
    限制总转弯次数不超过 $K$。
    需记录进入格子的方向以判断是否发生转弯。
```Python
# f[i][j][k][d] -> (i,j)坐标, k次转弯, d方向(0右, 1下)
f = [[[[0]*2 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

# 1. 初始化第一步（不计入转弯）
if M > 1 and g[0][1] == '.': f[0][1][0][0] = 1
if N > 1 and g[1][0] == '.': f[1][0][0][1] = 1

# 2. 状态转移
for i in range(N):
    for j in range(M):
        if g[i][j] == '#' or i + j <= 1: continue
        for p in range(K + 1):
            # 向右走：同向(p不变) + 转向(p-1)
            if j > 0:
                f[i][j][p][0] += f[i][j-1][p][0]
                if p > 0: f[i][j][p][0] += f[i][j-1][p-1][1]
            # 向下走：同向(p不变) + 转向(p-1)
            if i > 0:
                f[i][j][p][1] += f[i-1][j][p][1]
                if p > 0: f[i][j][p][1] += f[i-1][j][p-1][0]

# 3. 结果汇总
ans = sum(f[N-1][M-1][p][d] for p in range(K+1) for d in range(2))
```
## 带障碍物的路径计数 (Grid with Obstacles)

### 题目要求

在 $n \times m$ 的网格中，某些格子（标记为 `#`）无法通行，求从起点到终点的方案数。

### 核心修改点
在状态转移前，增加一个判断：如果当前格子是障碍物，直接跳过（该格方案数为 $0$）。
### 核心代码

```Python
# g 为存储地图的二维列表
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0 or g[i][j] == '#':
            continue
        
        if i > 0: dp[i][j] += dp[i-1][j]
        if j > 0: dp[i][j] += dp[i][j-1]
```

---

## 最大路径权值和 (Maximum Path Sum)

### 题目要求

每个格子 $(i, j)$ 都有一个分值 $v_{i,j}$，求从起点到终点所经过路径的得分总和最大是多少。

### 核心修改点

1. **目标改变**：将“求和”改为“求最大值” (`max`)。
    
2. **状态定义**：$dp[i][j]$ 表示到达 $(i, j)$ 的最大得分。
    
3. **初值处理**：除起点外，通常初始化为极小值（如 `-1` 或 `-float('inf')`）。
    

### 核心代码
```Python
# a 为各格子的分值矩阵
dp = [[-1] * m for _ in range(n)]
dp[0][0] = a[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0: continue
        
        up = dp[i-1][j] if i > 0 else -1
        left = dp[i][j-1] if j > 0 else -1
        
        if up != -1 or left != -1:
            dp[i][j] = max(up, left) + a[i][j]
```

---

## 允许斜向移动 (Diagonal Moves / King's Move)

### 题目要求

机器人不仅可以向右、向下移动，还可以向**右下角斜向**移动。

### 核心修改点

增加一个转移来源：$dp[i-1][j-1]$。

### 核心代码

```Python
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0: continue
        
        if i > 0: dp[i][j] += dp[i-1][j]           # 上方
        if j > 0: dp[i][j] += dp[i][j-1]           # 左方
        if i > 0 and j > 0: dp[i][j] += dp[i-1][j-1] # 左上方斜向
```

---


