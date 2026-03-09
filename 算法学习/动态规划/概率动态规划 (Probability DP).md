概率动态规划:它通常分为两类：**求概率**（从始点推终点）和**求期望**（通常从终点倒推始点）。
## 概率 DP 通用模板（求概率型）

### 1. 核心思想

- **状态定义**：$dp[k][state]$ 表示经过 $k$ 步后，到达 $state$ 状态的**概率**。
    
- **转移逻辑**：$当前概率 = \sum (上一步概率 \times 转移到当前的概率)$。
    
- **特性**：所有合法状态的概率之和在每一步演变中应保持 $\le 1$。
    

### 2. 代码实现结构 (Python 3.7.3)


```Python

import sys

# 1. 初始化
# n: 规模, k: 步数
f = [[0.0] * n for _ in range(n)] 
f[start_i][start_j] = 1.0 # 初始位置概率为 1

# 2. 递推
for _ in range(k):
    new_f = [[0.0] * n for _ in range(n)] # 滚动数组思想，只存当前步
    for i in range(n):
        for j in range(n):
            if f[i][j] > 1e-12: # 剪枝：概率极小时不处理
                # 遍历所有可能的下一步
                for ni, nj in get_next(i, j):
                    if is_valid(ni, nj):
                        # P_move 是转移概率（如 1/8）
                        new_f[ni][nj] += f[i][j] * P_move 
    f = new_f

# 3. 统计结果
ans = sum(map(sum, f))
```

---

# 题目
[[期望DP/808.分汤]]
[[期望DP/688.骑士在棋盘上的概率]]