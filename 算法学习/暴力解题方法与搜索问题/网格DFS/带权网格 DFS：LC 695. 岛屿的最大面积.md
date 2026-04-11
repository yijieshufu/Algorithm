# LC 695. 岛屿的最大面积
在 $n \times m$ 的二进制网格中，`1` 代表陆地，`0` 代表水。岛屿由水平或垂直方向相连的 `1` 构成。岛屿面积是其中 `1` 的个数。求网格中最大岛屿的面积。
# 分析
- **本质**：网格 DFS（深度优先搜索）统计连通块大小。
- **策略**：全盘扫描，每遇到一个 `1` 就启动一次 DFS。
- **动作**：
    1. **原地爆破**：进入 DFS 后立即将当前陆地 `1` 变为 `0`，既能标记已访问，又能防止重复计算，省去 `visited` 数组。
    2. **递归累加**：DFS 探索四个方向，递归返回各个方向的面积总和，加上当前格子的 `1`。
- **结果**：用 `ans` 记录全局最大面积。
# 代码
```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        g = grid
        n,m = len(g) ,len(g[0])
        ans = 0
        # 统计岛屿的大小 修改
        def dfs(r,c):
            g[r][c] = 0
            f = 1
            for x,y in ((0,1),(1,0),(-1,0),(0,-1)):
                a , b = r+x ,c+y
                if 0<=a<n and 0<=b<m and g[a][b]:
                    f += dfs(a,b)
            return f
        for i in range(n):
            for j in range(m):
                if g[i][j]: # 发现岛屿
                    a_area = dfs(i,j)
                    if a_area > ans : ans = a_area
        return ans
```