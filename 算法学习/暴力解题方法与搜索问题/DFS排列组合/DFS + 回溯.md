# [组合问题](https://www.lanqiao.cn/courses/52517/learning/?id=5027774&compatibility=false)
- **目标**：从 $1 \sim n$ 这 $n$ 个整数中，随机选取 $m$ 个数。
- **要求**：
    1. 输出所有可能的组合。
    2. 组合内部必须升序（例如选出 $\{1, 2\}$ 而不是 $\{2, 1\}$）。
    3. 所有组合按**字典序**输出。
- **数据规模**：$n, m \le 25$。组合数 $C_{25}^{12}$ 约为 520 万，DFS 暴力搜索在 Python 中约需 1~2 秒，加了剪枝后能稳过。
# 分析
组合枚举 DFS，传个 `start` 别回头，剪枝判剩余，字典序自成。
## 代码
```python
import os
import sys

it = iter(sys.stdin.read().split())
n,m = int(next(it)),int(next(it))

res =[]
def dfs(u,start):
  if u == m:
    print(*(res))
    return
  for i in range(start,n+1):
    if n-i+1 < m - u :break # 出口条件
    res.append(i)
    dfs(u+1,i+1) # 不回头
    res.pop()
dfs(0,1)
```
