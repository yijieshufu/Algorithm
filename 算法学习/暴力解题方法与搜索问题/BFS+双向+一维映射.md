# 迷宫-真题

- **核心动作**：在 $n \times n$ 的网格中，从所有格子均匀随机出发，求到达终点 $(n, n)$ 的最短步数期望值。
- **移动方式**：上下左右移动（代价 1）或使用 $m$ 个双向传送门（代价 1）。
- **数据边界**：$n, m \le 2000$。格点总数 $N^2 = 4 \times 10^6$。
# 分析
- **逆向思维**：与其计算每个点到终点的距离，不如**从终点 $(n, n)$ 出发跑一次 BFS**。这样只需一次搜索就能得到全图所有点到终点的最短步数。
- **期望值本质**：期望值 = $\frac{\text{所有格子的最短步数之和}}{\text{格子总数 } n^2}$。
- **性能瓶颈**：由于格点数高达 $4 \times 10^6$，必须使用**一维平铺**（将二维坐标转为一维索引）和**哨兵边界**来规避 Python 缓慢的越界检查和多维索引。
## 代码

```python
import sys 
it = iter(sys.stdin.read().split())
n,m= int(next(it)),int(next(it))
# 转化为一维
stride = n+2
size = stride*stride
dist = [-1] * size # 距离数组 [-1,-1,-1,···,-1]
for i in range(stride):
  dist[i] = dist[size-stride+i]  = -2 # 第一行 和 最后一行
  dist[i*stride] = dist[i*stride+n+1] = -2 # 第一列 和 最后一列

portals = [[] for _ in range(size)]
has_p = [False]*size
for _ in range(m):
  r1,c1,r2,c2 = int(next(it)),int(next(it)),int(next(it)),int(next(it))
  u = r1*stride+c1
  v = r2*stride+c2
  portals[u].append(v);portals[v].append(u)
  has_p[u] = has_p[v] = True

# 从(n,n) 
target = n*stride + n # 重点开始
dist[target] = 0  # 距离
q = [target]
head = 0 
offs = [1,-1,stride,-stride] # 四个方向
while head < len(q):
  u = q[head]
  head += 1 
  for o in offs: # 遍历四个方向
    v = u+o
    if dist[v] ==-1:
      dist[v] = dist[u]+1
      q.append(v)
  if has_p[u] :
    for v in portals[u]:
      if dist[v] ==-1:
        dist[v] = dist[u]+1
        q.append(v)
total_sum = 0
for r in range(1,n+1):
  start = r * stride +1
  total_sum += sum(dist[start:start+n])
print(f"{total_sum / (n * n):.2f}")   
```
