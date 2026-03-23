# 小怂爱水洼
**【材料】 (Materials)**
- **空间**：一个 $N \times M$ 的网格，每个格子存储水量 $a_{i,j}$。
- **定义**：
    - **小水洼**：$a_{i,j} > 0$ 的格子。
    - **大水洼**：上下左右相邻且水量均 $> 0$ 的“小水洼”集合（即一个连通块）。
- **规模**：$N, M \le 100$，总格子数 $10,000$。  
**【条件】 (Constraints)**
- **移动限制**：只能在水量 $> 0$ 的相邻格子间移动。这暗示你**无法**在不经过“旱地”（水量为 0）的情况下从一个大水洼跳到另一个。
- **收集规则**：进入格子即收集全部水，每个格子只收一次。
- **重置规则**：每到一个“新”的大水洼，之前的总量清零。这其实是在告诉你：**你只能在一个连通块内累加，不能跨块累加。**  
**【目的】 (Objective)**
- 找到所有连通块中，水量总和（权值和）最大的那一个，输出该最大值。
## 分析
就是取不同大水洼 最大的只值  
	不同大水洼 也就是连通分量
## 代码
```python
import os
import sys

from collections import deque
it = iter(sys.stdin.read().split())
n,m=int(next(it)),int(next(it))
g = [[int(next(it)) for _ in range(m)] for _ in range(n)]
vis = [[False]*(m) for _ in range(n)]
ans = 0 
for i in range(n): # 寻找连通分量
  for j in range(m):
    if g[i][j]>0 and not vis[i][j]: # 找到了
      vis[i][j]=True
      q=deque([(i,j)])
      curr_sum = 0
      while q: # BFS
        x,y = q.popleft()
        curr_sum+=g[x][y] # 弹出计算
        for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
          nx ,ny = x+dx,y+dy
          if 0<=nx<n and 0<=ny<m and not vis[nx][ny] and g[nx][ny]>0:
            vis[nx][ny]=True
            q.append((nx,ny)) # 访问了 加入
      ans = max(ans,curr_sum)
print(ans)
```
