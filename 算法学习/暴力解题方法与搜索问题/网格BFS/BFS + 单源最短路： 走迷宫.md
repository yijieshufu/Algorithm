# 走迷宫
- **地图**：$N \times M$ 的网格，1 代表可以通行的道路，0 代表障碍物墙壁。
- **任务**：从起点 $(x_1, y_1)$ 走到终点 $(x_2, y_2)$。
- **目标**：求**最少**需要走多少个格子（即最短路径长度）。
- **限制**：如果无法到达，输出 -1。
- **注意**：输入坐标通常是 1-indexed（从 1 开始），代码处理时需转为 0-indexed。
# 分析

## 代码

```python
import sys
it = iter(sys.stdin.read().split())
n, m = int(next(it)), int(next(it))
g = [[int(next(it)) for _ in range(m)] for _ in range(n)]
# a 存坐标，步数单独标记或原地修改
r1, c1 = int(next(it))-1, int(next(it))-1
r2, c2 = int(next(it))-1, int(next(it))-1

# 特判：起点就是终点
if (r1, c1) == (r2, c2):
    print(0)
    sys.exit()

a = [(r1, c1, 0)]
g[r1][c1] = 0
b = 0

while b < len(a):
    r, c, d = a[b]
    b += 1
    for x, y in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r+x, c+y
        if 0 <= nr < n and 0 <= nc < m and g[nr][nc]:
            # 极限点：入队瞬间判断，不用等出队
            if (nr, nc) == (r2, c2):
                print(d + 1)
                sys.exit()
            g[nr][nc] = 0
            a.append((nr, nc, d + 1))
print(-1)
```
