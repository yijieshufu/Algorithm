# 题目描述
- **核心动作**：在 $N \times N$ 棋盘放 $N$ 个皇后，求互不攻击（同行、同列、同斜线仅一君）的合法方案总数。
- **数据边界**：$N \le 10$。规模极小，暗示可使用指数级复杂度的**回溯法（DFS）**。
# 分析
- **算法/数据结构**：**DFS 回溯**。
- **为何适用**：每一行必须且只能放一个皇后，构成典型的决策树深度搜索。
- **通用骨架**：
```python
def dfs(step):
    if step == end: count += 1; return
    for choice in choices:
        if valid(choice):
            make_choice()
            dfs(step + 1)
            undo_choice()
```
- **定级**：基础题（经典算法入门）。
- **核心难点**：如何利用坐标关系 $O(1)$ 判定**斜线冲突**。

- **[块 1：状态与路径记录]**  
    使用 `col[i]` 记录第 $i$ 列是否占用；  
	使用 `dg[u+i]` 记录正对角线（右上到左下，$row+col$ 为定值）；  
	使用 `udg[u-i+n]` 记录反对角线（左上到右下，$row-col$ 为定值，加 $n$ 防止负索引）。
- **[块 2：核心搜索逻辑]**  
    逐行放置。对于第 `u` 行，遍历每一列 `i`。若列与两条斜线均未被占用，则放置皇后并进入下一行。
- **[块 3：回溯恢复]**  
    当 `dfs` 递归返回时，必须将 `col`、`dg`、`udg` 的标记重置为 `False`，以便进行同层其他分支的尝试。

**行深列广，斜线定值**：每一行递归深入，每一列循环尝试，利用 `r+c` 和 `r-c+n` 的唯一性瞬间判定斜线冲突。

## 代码

```python
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
col = [0] * 20   # 块1：列标记
dg = [0] * 40    # 块1：正对角线 r+c
udg = [0] * 40   # 块1：反对角线 r-c+n
ans = 0
def dfs(u):
    global ans
    if u == n:   # 块3：到达边界
        ans += 1
        return
    for i in range(n): # 块2：遍历当前行的每一列
        if not col[i] and not dg[u+i] and not udg[u-i+n]:
            col[i] = dg[u+i] = udg[u-i+n] = 1 # 标记占用
            dfs(u + 1)
            col[i] = dg[u+i] = udg[u-i+n] = 0 # 块3：回溯还原
dfs(0)
print(ans)
```
