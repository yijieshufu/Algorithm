# 题目
- **核心动作**：在 $N \times M$ 的 A/B 迷宫中，按照 **“$K$ 个 A $\to$ $K$ 个 B”** 的周期节奏移动，求到达右下角 $(N-1, M-1)$ 的最少步数。
- **数据边界**：$N, M \le 1000, K \le 10$。总状态数高达 $10^7$，在 Python 中必须使用一维数组和 `bytearray` 优化内存。
# 分析
**[块 1：节奏状态定义]**  
普通的 BFS 只要知道坐标 $(r, c)$，但本题需要知道你正处于 $2K$ 周期中的第几拍（记为 `cur_k`）。
- 若 $0 \le \text{下一拍} < K$：目标格必须是 'A'。
- 若 $K \le \text{下一拍} < 2K$：目标格必须是 'B'。  
**[块 2：空间压缩与 bytearray]**  
为了防止内存超限（MLE），我们不使用三维数组 `vis[N][M][2K]`。
- **技巧 1**：使用 `bytearray`，每个元素仅占 1 字节。
- **技巧 2**：坐标压缩公式：`idx = (r * M + c) * K + (step % K)`。
- **原理**：因为 A 格子只会在 A 拍出现，B 格子只会在 B 拍出现，它们可以复用这 $K$ 个“抽屉”而不会冲突。  
**[块 3：BFS 搜索流程]**  
使用队列（`deque`）进行层序遍历。每次弹出一个点，检查四周。如果四周的字母符合当前节奏且该状态未被访问，则加入队列。

## 代码

```python
import sys
from collections import deque

# 极简 I/O：一次性读取所有数据
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
k = int(next(it))
grid = [next(it) for _ in range(n)]

# [块 1 & 2]：初始化。c=0 表示第一拍，d=0 表示步数
q = deque([(0, 0, 0, 0)])

# [块 2]：使用 bytearray 极致节省内存，初始点标记为已访问
# 总长度为 N * M * K
vis = bytearray(n * m * k)
vis[0] = 1 

ans = -1
while q:
    r, c, cur_k, d = q.popleft()
    
    # [块 3]：到达终点立即停止
    if r == n - 1 and c == m - 1:
        ans = d
        break
        
    # 计算下一拍是什么，以及那一拍对应的目标字符
    nxt_k = (cur_k + 1) % (2 * k)
    target = 'A' if nxt_k < k else 'B'
    
    # 尝试四个方向
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        
        # 1. 越界检查 2. 字符匹配
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == target:
            # [块 2]：计算压缩后的索引 (节拍取余保证在 K 范围内)
            idx = (nr * m + nc) * k + (nxt_k % k)
            if not vis[idx]:
                vis[idx] = 1
                q.append((nr, nc, nxt_k, d + 1))

print(ans)
```
