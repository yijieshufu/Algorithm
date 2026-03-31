# N皇后
- **核心动作**：在 $N \times N$ 棋盘放 $N$ 个皇后，求互不攻击（同行、同列、同斜线仅一君）的**合法方案总数**。
- **数据边界**：$N \le 10$。规模极小，暗示可使用指数级复杂度的**回溯法（DFS）**。
# 分析
**正斜线 ($/$)**：在这条线上的所有格子，**行号 + 列号 ($r+c$) 是一个常数**  
**反斜线 ($\backslash$)**：在这条线上的所有格子，**行号 - 列号 ($r-c$) 是一个常数**。
## 代码

```python
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
col = [0] * 20   
dg = [0] * 40    
udg = [0] * 40  
ans = 0
def dfs(u):
    global ans
    if u == n:   
        ans += 1
        return
    for i in range(n): 
        if not col[i] and not dg[u+i] and not udg[u-i+n]:
            col[i] = dg[u+i] = udg[u-i+n] = 1 
            dfs(u + 1)
            col[i] = dg[u+i] = udg[u-i+n] = 0 
dfs(0)
print(ans)
```
