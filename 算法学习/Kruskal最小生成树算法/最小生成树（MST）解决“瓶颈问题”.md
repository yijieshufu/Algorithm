# 电动车-真题
**【材料】 (Materials)**
- **基础数据**：$N$ 座城市，$M$ 条双向道路。
- **边权**：每条道路消耗电量 $w_i$。
- **规模**：$N, M \le 2 \times 10^5$，电量可达 $10^9$。这是一个大规模数据，要求算法复杂度在 $O(M \log M)$ 或 $O(M \log N)$。  
**【条件】 (Constraints)**
- **充电机制**：出发城市及任何中途经过的城市都可以充满电。这意味着你只需要保证**任何一条单程道路**的花费不超过电池容量即可。
- **目标**：任意两个城市之间都必须存在路径（全连通）。
- **判定**：如果不连通，输出 $-1$。  
**【目的】 (Objective)**
- 寻找一个最小的容量 $L$，使得只使用花费 $w_i \le L$ 的道路，整张图是连通的。
## 🧠 逻辑分析：为什么是最小生成树？
1. **直观理解**：为了让电池容量尽可能小，我们要优先选择那些省电（权值小）的路来连接城市。
2. **瓶颈问题**：两点之间路径上的“最大边权”决定了你需要的电池容量。要让这个“最大值”在所有可能的路径中最小，这正是**最小生成树（MST）** 的特性。
3. **结论**：在最小生成树中，最后一条让全图连通的边的权值，就是我们要找的答案。

排序  
	优先使用权重小的  
	直到连通为1
## 代码

```python
import sys
# 数据读入
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a = []
for _ in range(m):
  u,v,w = int(next(it)),int(next(it)),int(next(it))
  a.append((w,u,v))
a.sort()
f = list(range(n + 1))
g=n # 连通块个数 目标是减到1
ans = 0 
for w,u,v in a:
  if g==1:break
  ra, rb = u, v # 各自的根节点
  while ra!=f[ra]:
    f[ra] = f[f[ra]]
    ra = f[ra]
  while rb!=f[rb]:
    f[rb] = f[f[rb]]
    rb = f[rb]
  if ra !=rb:
    f[ra] = rb
    ans = w
    g-=1

if n==1:
  print(n)
else:
  print(ans)
```
