# 混境之地2
- **空间**：一个 $n \times m$ 的网格地图。
    - `.` 表示道路（可通行）。
    - `#` 表示墙壁（不可通行）。
- **点位**：起点坐标 $(A, B)$，终点坐标 $(C, D)$。

- **触发时机**：当你面对 `#` 时，可以选择消耗技能通过，此后便只能走 `.`。只能用一次  
从起点 $(A, B)$ 走到出口 $(C, D)$。
## 分析
#### 1. 遇到“迷宫最短/可行路径” $\rightarrow$ 想到“广度优先搜索 (BFS)”
使用 deque 来实现：先进先出  
	用来做BFS 刚好合适
#### **2.遇到“技能只能用一次” $\rightarrow$ 想到“状态空间扩展”**
采用 元组集合 (Set of Tuples)：  
	`g = set([(start_x, start_y, 0)])`  
	- **`(x, y, 0)`**：表示你带着技能到达了 $(x, y)$。  
	- **`(x, y, 1)`**：表示你失去技能后到达了 $(x, y)$。
#### **3. 遇到“墙壁 `#`” $\rightarrow$ 想到“条件转移”**
- **逻辑**：
    - 如果邻居是 `.` $\rightarrow$ 直接走，状态 `state` 不变。
    - 如果邻居是 `#` **且** 当前 `state == 0` $\rightarrow$ 消耗技能，状态变为 `1`。
## 代码
```python
import os
import sys
from collections import deque

it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
q= deque([(int(next(it))-1,int(next(it))-1,0)]) # 存入起点 下标从0开始
a , b = int(next(it))-1,int(next(it))-1 #终点
f = [next(it) for _ in range(n)] #做判断用 直接存入字符串就可以 但是下标是从0开始的
g = set([(q[0][0],q[0][1],0)]) # 存入访问过的
ans = "No"
while q:
  r,c,k = q.popleft()
  if r == a and c ==b: ans = "Yes";break
  for dr,dc in [(1,0),(0,1),(0,-1),(-1,0)]:
    nr ,nc = r+dr,c+dc
    if 0<=nr<n and 0<=nc<m:
      if f[nr][nc] == '.'and (nr,nc,k) not in g:
        g.add((nr,nc,k))
        q.append((nr,nc,k))
      elif f[nr][nc] == '#'and k==0 and (nr,nc,1) not in g:
        g.add((nr, nc, 1))
        q.append((nr, nc, 1))
print(ans)
```

|**符号**|**竞赛中的含义**|**例子**|
|---|---|---|
|**`()` 元组**|**打包状态**。把 $x, y, k$ 绑在一起当成一个点。|`(nx, ny, 1)`|
|**`[]` 列表**|**初始化容器**。给 `deque` 或 `set` 提供初始数据。|`deque([起点])`|
|**`[]` 下标**|**精准定位**。访问第 $i$ 个元素或第 $j$ 列。|`f[r][c]`|