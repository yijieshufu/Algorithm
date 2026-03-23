# 混境之地5
**【材料】 (Materials)**
- **空间**：一个 $n \times m$ 的网格，每个点有高度 $h_{ij}$。
- **起始/终点**：从 $(A, B)$ 出发，目标是到达 $(C, D)$。
- **道具**：喷气背包，使用后当前高度临时增加 $k$。
- **规模**：$n, m \le 1000$，高度可达 $10^6$。  
**【条件】 (Constraints)**
- **移动规则**：上下左右移动。
- **高度限制**：只能向高度**严格低于**当前高度的方向走。
- **资源限制**：喷气背包**只能使用一次**。
- **逻辑细节**：
    - 普通移动：$h_{next} < h_{curr}$。
    - 跳跃移动（使用背包）：$h_{next} < h_{curr} + k$。使用后，你到达新地点，高度变回该地点的原始高度，且背包失效。  
**【目的】 (Objective)**
- 判断是否能到达出口，输出 `Yes` 或 `No`。
## 分析

背包 分为 两种情况：  
	使用了两个访问数组  
	使用背包：访问数组0  
	未使用背包：访问数组1
## 代码
```python
import os
import sys
from collections import deque
it = iter(sys.stdin.read().split())
n,m,k= int(next(it)),int(next(it)),int(next(it))
a = [int(next(it))-1 for _ in range(4)] # 下标从0 
h = [[int(next(it)) for _ in range(m)] for _ in range(n)] # 高度 下标从0 开始
v0 = [[0] * m for _ in range(n)]
v1 = [[0] * m for _ in range(n)]
q = deque([(a[0],a[1],0)])
v0[a[0]][a[1]]=1
ans="No"
while q:
  r,c,s= q.popleft()
  if r ==a[2] and c ==a[3] :
    ans = "Yes";break
  cur_h = h[r][c]
  for dr,dc in [(0,1),(-1,0),(1,0),(0,-1)]:
    nr,nc = r+dr,c+dc
    if 0<=nr<n and 0<=nc<m:
      if s ==0: # 未使用背包  
        if h[nr][nc] <cur_h and not v0[nr][nc]:
          v0[nr][nc]=1
          q.append((nr,nc,0))
        if h[nr][nc] < cur_h+k and not v1[nr][nc]:
          v1[nr][nc]=1
          q.append((nr,nc,1))
      else:
        if h[nr][nc] <cur_h and not v1[nr][nc]:
          v1[nr][nc]=1
          q.append((nr,nc,1))
print(ans)
```