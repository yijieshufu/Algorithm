# 像素放置
- **场景**：在一个 $n \times m$ 的网格中填入 **0（白色）** 或 **1（黑色）**。
- **约束条件**：部分格子标有数字 $x$（$0 \le x \le 9$）。该数字表示：以该格子为中心的 $3 \times 3$ 区域内（包含自身及周围 8 个方向），黑色格子的总数必须恰好等于 $x$。
- **目标**：在满足所有数字约束的前提下，给出唯一的全盘填充方案。
- **数据规模**：$n, m \le 10$。虽然状态空间 $2^{100}$ 极大，但约束条件非常密集，适合使用带剪枝的 DFS。

# 分析 
这道题最本质的优化在于：**不要等全盘填完再检查，而是在约束条件被“填满”的一瞬间立即检查。**
- **判定时机**：对于坐标为 $(i, j)$ 的数字约束，它影响的范围最远到 $(i+1, j+1)$。
- **预处理 (`todo`)**：当我们按照从左到右、从上到下的顺序填到格子 $(r, c)$ 时，如果某个数字约束 $(i, j)$ 满足 $i+1 = r$ 且 $j+1 = c$，说明该约束覆盖的 9 个格子已经全部确定。
- **即时剪枝**：在 DFS 填入 $(r, c)$ 后，立即计算对应约束区域的和。如果不等于 $x$，说明当前分支非法，直接回溯。
# 代码

```python
import sys 
it = iter(sys.stdin.read().split())
n,m = int(next(it)),int(next(it))
g = [next(it) for _ in range(n)]

ans = [[0]*m for _ in range(n)]
todo = [[[] for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if g[i][j] != '_':
      # 约束 (i, j) 涉及到的最右下角坐标
      r_limit, c_limit = min(n - 1, i + 1), min(m - 1, j + 1)
      todo[r_limit][c_limit].append((i, j))
def dfs(p):
  if p == n*m: # 
    for row in ans :
      print("".join(map(str,row)))
    return True
  r,c = divmod(p,m) # 返回 p//m 和p % m
  for v in (0,1):
    ans[r][c] = v 
    ok = True
    for tr,tc in todo[r][c]:
      s = 0
      # 计算着9个点
      for i in range(max(0,tr - 1),min(n,tr+2)):
        for j in range(max(0,tc - 1),min(m,tc+2)):
          s+=ans[i][j]
      if s!=int(g[tr][tc]):
        ok = False
        break
    if ok and dfs(p+1):
      return True
  return False
dfs(0)
```

