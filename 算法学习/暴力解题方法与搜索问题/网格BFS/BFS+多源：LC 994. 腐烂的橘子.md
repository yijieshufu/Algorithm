# LC 994. 腐烂的橘子
在 $n \times m$ 网格中，0为空地，1为新鲜橘子，2为腐烂橘子。  
每分钟腐烂橘子会向上下左右四个方向传染新鲜橘子  
求所有橘子**变腐烂的最短分钟数**。若不可能，返回 -1。

# 分析
- **本质**：多源 BFS（广度优先搜索）。所有初始腐烂的橘子都是起点，同步向外扩散。
- **初始状态**：遍历全图，将所有腐烂橘子（值为2）的坐标和初始时间 0 压入队列 `a`，并统计新鲜橘子总数 `f`。
- **波纹扩散**：利用游标 `b` 遍历队列 `a`。每传染一个新鲜橘子，`f` 减 1，并将新坐标及增加后的分钟数压入队尾。
- **结果判定**：若最终新鲜橘子数 `f` 为 0，返回最后弹出的分钟数 `ans`；否则返回 -1。
# 代码

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        g = grid
        n,m = len(g),len(g[0]) # 行 和 列
        a,f,b,ans = [],0,0,0
        # 统计 起点 和 新鲜数
        for i in range(n):
            for j in range(m):
                if g[i][j] ==2:a.append((i,j,0))
                if g[i][j] ==1:f+=1
        while b<len(a):
            r,c,ans = a[b]
            b+=1
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                ni ,nj = r+x,c+y
                if 0<=ni<n and 0<=nj<m and g[ni][nj] ==1:
                    g[ni][nj] = 2 
                    f -=1
                    a.append((ni,nj,ans+1))
        return ans if f==0 else -1
```