# LC 542. 01 矩阵
给定一个由 0 和 1 组成的矩阵 `mat`，求每个格子到最近的 0 的距离。相邻格子距离为 1。
# 分析
- **本质**：多源 BFS（广度优先搜索）。
- **策略**：将所有 0 看作起点同时出发。
- **实现**：
    1. 初始化 `ans` 矩阵：0 处记为 0，1 处记为 -1（表示未访问）。
    2. 将所有 0 的坐标压入队列 `a`。
    3. 利用游标 `b` 模拟队列弹出，向四个方向扩散。
    4. 若邻居为 -1，则更新距离为 `当前距离 + 1` 并入队。
# 代码
```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        g = mat
        n, m = len(g), len(g[0])
        # ans: 结果矩阵，-1代表未访问
        ans = [[-1] * m for _ in range(n)]
        # a: 队列, b: 游标
        a, b = [], 0
        
        # 1. 初始多源点入队
        for i in range(n):
            for j in range(m):
                if not g[i][j]:
                    ans[i][j] = 0
                    a.append((i, j))
        # 2. BFS 扩散
        while b < len(a):
            r, c = a[b] #由 0 位置 推算周边没有访问过的
            b += 1
            # 修正后的 4 方向：下、上、右、左
            for x, y in ((1,0), (-1,0), (0,1), (0,-1)):
                f, g_v = r + x, c + y # f: 行坐标, g_v: 列坐标
                if 0 <= f < n and 0 <= g_v < m and ans[f][g_v] == -1:
                    ans[f][g_v] = ans[r][c] + 1
                    a.append((f, g_v))
        return ans
```
