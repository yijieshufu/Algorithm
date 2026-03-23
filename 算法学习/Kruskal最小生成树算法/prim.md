# 爆破-真题
**【材料】 (Materials)**
- **对象**：$n$ 个圆，每个圆由圆心 $(x_i, y_i)$ 和半径 $r_i$ 组成。
- **连接成本（边权）**：
    - 如果两个圆相交或相切：成本为 **0**。
    - 如果两个圆不相交：成本为**边缘之间的最短距离**，即 $d_{ij} = \sqrt{(x_i-x_j)^2 + (y_i-y_j)^2} - (r_i + r_j)$。
- **规模**：$n \le 5000$。这意味着总边数可能达到 $\frac{5000 \times 4999}{2} \approx 1.25 \times 10^7$（完全图）。
    
**【条件】 (Constraints)**
- **全连通**：所有魔法阵必须能一起引爆（即处于同一个连通分量）。
- **最优性**：要求魔法回路的总长度**最小**。
- **精度**：输出保留两位小数。  
**【目的】 (Objective)**
- 在所有魔法阵构成的完全图中，求出**最小生成树**的总权重。
## 🧠 逻辑分析：遇到了什么 $\rightarrow$ 想到什么
#### **1. 遇到“连接所有点且总和最小” $\rightarrow$ 想到“最小生成树”**
由于这是一个**稠密图**（任意两个圆之间都有定义的距离），**Prim 算法**比 Kruskal 算法更适合，因为 Prim 的复杂度 $O(V^2)$ 只与点数有关，而 Kruskal 的 $O(E \log E)$ 在边数巨大的情况下开销极大。
#### **2. 遇到“圆的边缘距离” $\rightarrow$ 想到“距离公式转化”**
两个圆心之间的距离为 $D = \sqrt{\Delta x^2 + \Delta y^2}$。  
电路长度 $w = \max(0, D - r_1 - r_2)$。
#### **3. 遇到 $N=5000$ 的 Python 挑战 $\rightarrow$ 想到“性能压榨”**
在 Python 中跑 2500 万次循环非常吃力。为了过题，我们需要：
- 尽量减少循环内的冗余计算。
- 使用 Prim 算法并在寻找最小距离点时保持逻辑精简。

## 代码
```python
import sys
import math

# [起手式：标准 I/O 与数据打包]
it = iter(sys.stdin.read().split())
n = int(next(it))
a = []
for _ in range(n):
  a.append([float(next(it)),float(next(it)),float(next(it))])

f = [0]*n 
g = [1e18]*n  # 距离 初始化最大值 1e18
g[0]=0
ans = 0 
# prim
for _ in range(n):
  u =-1
  for i in range(n): #顺序找个节点开始
    if not f[i] and (u ==-1 or g[i]<g[u]): #枚举
      u = i
  if g[u] == 1e18: break
  f[u]=1
  ans += g[u] #理解代价
  ux,uy,ur = a[u]
  for v in range(n):# 枚举所有的点
    if not f[v]:
      vx,vy,vr = a[v]
      d = ((ux-vx)**2+(uy-vy)**2)**0.5 - ur - vr 
      if d<0:d=0
      if d < g[v]:
        g[v]=d
print("%.2f"%ans)
```