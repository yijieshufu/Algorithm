# N皇后
- **核心动作**：在 $N \times N$ 棋盘放 $N$ 个皇后，求互不攻击（同行、同列、同斜线仅一君）的**合法方案总数**。
- **数据边界**：$N \le 10$。规模极小，暗示可使用指数级复杂度的**回溯法（DFS）**。
# 分析
**坐标变换判重（$O(1)$ 冲突检测）。**
- **列冲突**：直接用列号 `i`。
- **正斜线 (/) 冲突**：同一条线上的格子 `行号 + 列号` 是常数，即 `u + i`。
- **反斜线 () 冲突**：同一条线上的格子 `行号 - 列号` 是常数。为了防止负数，统一加个偏移量，即 `u - i + n`。
## 代码
```python
import sys
# 1. 极简读入
it = iter(sys.stdin.read().split())
n = int(next(it))
# 2. 变量定义：a(列), f(正斜线), g(反斜线), ans(计数)
a, f, g = [0]*20, [0]*40, [0]*40
ans = 0
# 3. 极简 DFS
def dfs(u): # u 代表当前处理第 u 行
    global ans
    if u == n:
        ans += 1
        return
    for i in range(n): # i 代表尝试放在第 i 列
        # 冲突检查：列、正斜、反斜都没被占领
        if not a[i] and not f[u+i] and not g[u-i+n]:
            # 过河拆桥：原地标记占领
            a[i] = f[u+i] = g[u-i+n] = 1
            dfs(u + 1)
            # 吐出来：回溯撤销
            a[i] = f[u+i] = g[u-i+n] = 0

dfs(0)
print(ans)
```
