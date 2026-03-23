# 仙境诅咒
**【材料】 (Materials)**
- **对象**：$N$ 个修仙者（点），每个点有坐标 $(X_i, Y_i)$。
- **传播源**：第 1 位修仙者（妮妮）。
- **传播媒介**：欧几里得距离。
- **传播范围**：距离 $D$ 以内的修仙者。
- **规模**：$N \le 1000$，坐标范围 $\pm 1000$。这意味着 $O(N^2)$ 的距离计算量（100 万次）是完全可以接受的。  
**【条件】 (Constraints)**
- **连锁反应**：只要 A 被诅咒且 B 在 A 的 $D$ 范围内，B 就会被诅咒。这是一个**传递性**的过程。
- **距离判定**：$\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2} \le D$。为了提高效率和精度，通常直接对比 $(x_1-x_2)^2 + (y_1-y_2)^2 \le D^2$。

**【目的】 (Objective)**
- 预测哪些修仙者**最终会被诅咒** ，被访问到了
## 分析
连锁传播/感染” $\rightarrow$ 想到 用 “**图的遍历 (BFS/DFS)**”
## 代码
```python
import os
import sys
from collections import deque
it = iter(sys.stdin.read().split())
n = int(next(it))
g = []
for _ in range(n):
  g.append((float(next(it)),float(next(it))))
d = float(next(it))
d2 = d*d
vis = [0]*n
vis[0] = 1
q = deque([0]) # 已经访问的（感染）编号
while q:
  u = q.popleft()
  x1,y1 = g[u]
  for v in range(n):# 判断所以距离是否满足条件
    if vis[v]==0:
      x2,y2=g[v]
      if (x2-x1)**2+(y2-y1)**2 <=d2:
        q.append(v)
        vis[v]=1
for res in vis:
  print(res)
```
