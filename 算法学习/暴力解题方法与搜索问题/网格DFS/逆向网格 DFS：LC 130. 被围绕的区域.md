# LC 130. 被围绕的区域
将矩阵中所有被 `X` 围绕的 `O` 填充为 `X`。  
若 `O` 处于边界或与边界的 `O` 连通，则它处于“安全区”，不被填充。

# 分析
- **本质**：**逆向思维（围魏救赵）**。  
	与其找哪些 `O` 被包围，不如找哪些 `O` 绝对安全。
- **策略**：从矩阵的 **四个边界** 出发，只要遇到 `O`，就通过 DFS 把所有与之相连的 `O` 暂时改写为标记位 `#`（代表安全区）。
- **清算**：遍历全盘。剩下的 `O` 说明没被标记，必被包围，改写为 `X`；标记位 `#` 恢复为 `O`。
# 代码
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        g = board
        n, m = len(g), len(g[0])

        # 1. 函数定义：只负责标记
        def dfs(r, c):
            g[r][c] = '#'
            for x, y in ((0,1), (1,0), (0,-1), (-1,0)):
                f, b = r+x, c+y
                if 0 <= f < n and 0 <= b < m and g[f][b] == 'O':
                    dfs(f, b)
        
        # 2. 边界触发（点火）
        for i in range(n):
            if g[i][0] == 'O': dfs(i, 0)
            if g[i][m-1] == 'O': dfs(i, m-1)
        for j in range(m):
            if g[0][j] == 'O': dfs(0, j)
            if g[n-1][j] == 'O': dfs(n-1, j)

        # 3. 全盘清算
        for i in range(n):
            for j in range(m):
                if g[i][j] == 'O': g[i][j] = 'X'
                if g[i][j] == '#': g[i][j] = 'O'
```