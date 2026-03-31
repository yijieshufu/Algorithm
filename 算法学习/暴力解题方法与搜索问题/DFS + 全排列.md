# 题目描述
- **核心动作**：在 $1 \le n \le 8$ 的极小数据下，按**字典序**穷举并输出 $1 \sim n$ 的所有全排列。
- **数据边界**：$n$ 最大仅为 8，全排列总数 $8! = 40,320$，计算量在 $10^5$ 级，Python 可在 1s 内轻松完成。
# 分析
全排列必用 DFS，从小到大枚举保序，递归归来务必“恢复现场”（`st[i]=False`）。
## 代码

```python
import sys

# 输入流初始化
it = iter(sys.stdin.read().split())
n = int(next(it))

# 认知块 1：定义路径与状态位
path = [0] * n
st = [False] * (n + 1)

def dfs(u):
    # 认知块 3：递归终止，输出结果
    if u == n:
        print(*(path))
        return
    # 认知块 2：按 1~n 顺序枚举，确保字典序
    for i in range(1, n + 1):
        if not st[i]:
            path[u] = i
            st[i] = True   # 标记使用
            dfs(u + 1)     # 向下递归
            st[i] = False  # 恢复现场 (回溯关键)

# 执行入口
dfs(0)
```
