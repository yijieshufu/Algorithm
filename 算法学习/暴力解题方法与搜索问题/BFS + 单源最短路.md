# 走迷宫
- **地图**：$N \times M$ 的网格，1 代表可以通行的道路，0 代表障碍物墙壁。
- **任务**：从起点 $(x_1, y_1)$ 走到终点 $(x_2, y_2)$。
- **目标**：求**最少**需要走多少个格子（即最短路径长度）。
- **限制**：如果无法到达，输出 -1。
- **注意**：输入坐标通常是 1-indexed（从 1 开始），代码处理时需转为 0-indexed。
# 分析
1. **初始化**：创建一个**队列**（Queue）存放待探索的坐标，以及一个**距离矩阵**（`dist`），初始值设为 `-1`（代表未访问过）。
2. **起点入队**：将起点坐标压入队列，并标记 `dist[起点] = 0`。
3. **波纹扩散（核心）**：
    - 从队首取出一个格子，尝试向上下左右 **4个方向** 移动。
    - 如果新格子在地图内、是路（1）、且没走过（`dist == -1`），则将其步数设为“当前格子步数 + 1”，然后放入队尾。
4. **终点判定**：由于 BFS 是按“层”扩展的，**第一次**弹出终点坐标时，记录的步数必然是全局最短步数。
5. **结束**：若队列为空仍未搜到终点，说明无法到达，输出 `-1`。
## 代码

```python
import os
import sys
from collections import deque

# 请在此输入您的代码
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
g = [[int(next(it)) for _ in range(m)] for _ in range(n)]
x1= int(next(it))-1;y1= int(next(it))-1;x2= int(next(it))-1;y2= int(next(it))-1
dist = [[-1] * m for _ in range(n)]
queue = deque([(x1,y1)])
dist[x1][y1]=0
found= False
while queue:
  cur_x,cur_y=queue.popleft()
  if cur_x==x2 and cur_y==y2:
    found=True
    print(dist[cur_x][cur_y])
    break
  for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
    nx=cur_x+dx;ny=cur_y+dy
    if 0<=nx<=n-1 and 0<=ny<=m-1: # 边界条件判断
      if g[nx][ny]==1 and dist[nx][ny]==-1 : # 有路并且 没有走过
        dist[nx][ny]= dist[cur_x][cur_y]+1
        queue.append((nx,ny)) # 压入走过的路
if not found:
  print(-1)  
```
