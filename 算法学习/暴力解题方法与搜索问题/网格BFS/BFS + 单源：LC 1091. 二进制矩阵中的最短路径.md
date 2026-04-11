# 1091. 二进制矩阵中的最短路径
在 $n \times n$ 的二进制网格中，寻找从左上角 $(0,0)$ 到右下角 $(n-1, n-1)$ 的最短路径长度。  
只能在值为 `0` 的格子上移动，支持 8 个方向（含对角线）。  
无法到达返回 -1。
# 分析
`a= []` 记录处理的元素  
直接在地图上写出 到达最小的距离
# 代码
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        g, n = grid, len(grid)
        # 拦截：起点或终点是墙
        if g[0][0] or g[n-1][n-1]: return -1
        # 特判：1x1 的情况
        if n == 1: return 1
        
        # a: 队列, b: 指针, g[0][0]: 起点步数
        a, b, g[0][0] = [(0, 0)], 0, 1
        
        while b < len(a):
            m, f = a[b]
            b += 1
            # 8个方向极简遍历
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    # 只有格子是 0 且不越界才进场
                    if 0 <= m+i < n and 0 <= f+j < n and not g[m+i][f+j]:
                        g[m+i][f+j] = g[m][f] + 1
                        # 【最关键】入队瞬间判断，直接截断
                        if m+i == n-1 and f+j == n-1:
                            return g[m+i][f+j]
                        a.append((m+i, f+j))
        return -1
```