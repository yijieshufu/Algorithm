# 200. 岛屿数量

**题目描述**：  
给你一个 $n \times m$ 的网格 `grid`，`1` 代表陆地，`0` 代表水。计算岛屿的数量（连通的 `1` 的个数）。  
**极简分析**：
- **本质**：全盘扫描 + 发现陆地即触发“爆破模式”。
- **动作**：每当遇到一个 `1`，答案 `ans + 1`，然后用 DFS 把与之相连的所有 `1` 全部砸成 `0`。
# 代码
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        g,ans = grid,0 
        n,m = len(g), len(g[0]) # 行 列 
        
        def dfs(r,c):
            g[r][c] ='0' # 陆地 变水
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = r+x ,c+y
                if 0<= nr < n and 0<=nc< m and g[nr][nc] =='1':
                    dfs(nr,nc)
        for i in range(n):
            for j in range(m):
                if g[i][j] =="1":
                    ans+=1
                    dfs(i,j)
        return ans 
```