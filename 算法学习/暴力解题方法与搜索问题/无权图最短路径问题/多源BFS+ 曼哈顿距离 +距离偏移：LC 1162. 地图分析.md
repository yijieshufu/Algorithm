# LC 1162. 地图分析
在一个 $n \times n$ 的网格中，`1` 代表陆地，`0` 代表海洋。  
找出一个海洋单元格，使得它距离最近的陆地单元格的距离最大，并返回该距离。  
如果网格只有陆地或只有海洋，返回 `-1`。  
距离采用曼哈顿距离。
# 分析
### 1. 为什么 BFS 等于曼哈顿距离？
曼哈顿距离的定义是：$|x_1 - x_2| + |y_1 - y_2|$。  
在棋盘格里，你只能上下左右走，每走一步，这个公式的值就正好 **+1**。
- **第 1 层扩散**：走的步数是 1，曼哈顿距离也是 1。
- **第 2 层扩散**：走的步数是 2，曼哈顿距离也是 2。
- **第 n 层扩散**：走的步数是 n，曼哈顿距离也是 n。
# 代码

```python

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        g , n = grid ,len(grid)
        q  = [] 

        # 海洋 找 陆地 ？ 那我写成 陆地 找 海洋
        for i in range(n):
            for j in range(n):
                if g[i][j]:q.append((i,j))
        # 题目要求的特殊条件
        if not q or len(q) == n*n: return -1
        ans = -1
        h = 0
        while h < len(q):
            r,c = q[h]
            h+=1
            for x,y in ((0,1),(1,0),(-1,0),(0,-1)):
                a,b = r+x,c+y
                if 0 <= a < n  and 0 <= b < n and g[a][b] ==0:
                    g[a][b] = g[r][c] + 1
                    ans  = max(ans,g[a][b]-1) # 距离比曼哈顿距离多了 1 
                    q.append((a,b))
        return ans 
```