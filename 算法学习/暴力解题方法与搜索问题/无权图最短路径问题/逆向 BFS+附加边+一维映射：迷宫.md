# 迷宫-真题

- **核心动作**：在 $n \times n$ 的网格中，从所有格子**均匀随机出发**，求到达终点 $(n, n)$ 的最短步数期望值。
- **移动方式**：上下左右移动（代价 1）或 使用 $m$ 个双向传送门（代价 1）。
# 分析
核心本质：空间换时间 + 极简字典
1. **一维平铺**：Python 的 `g[r][c]` 慢到离谱，必须用 `g[u]`。
2. **字典传送门**：别开 $4 \times 10^6$ 的列表套列表，用 `p = {}`，只有有传送门的地方才占空间。
3. **哨兵逻辑**：为了省掉 `if 1 <= r <= n`，直接把数组开大一圈，**不给它赋值 `-1`**（默认为 $0$ 或 $-2$），这样 `if g[v] == -1` 就会自动跳过边界。
## 代码

```python
import sys 
it = iter(sys.stdin.read().split())
n,m = int(next(it)),int(next(it))
s = n+2
g = [-2] *(s*s) # 建立 路径图
p = {} # 传送门
for i in range(1,n+1): 
    start = i*s + 1
    g[start:start+n] = [-1] * n
for _ in range(m):  
    u = int(next(it))*s + int(next(it)) # 转化为一维坐标
    v = int(next(it))*s + int(next(it))
    p[u] = p.get(u,[]) + [v] # 存入边
    p[v] = p.get(v,[]) + [u]

# 逆向
start_node = n*s+n
g[start_node] = 0
q = [start_node] 
h = 0
while h < len(q):
    u = q[h]
    h+=1
    d_next = g[u]+1
    # 1:四个方向走
    for o in (1,-1,-s,s):
        v = u + o
        if g[v] ==-1:
            g[v] = d_next
            q.append(v)
    # 2：走传送门
    if u in p:
        for v in p[u]:
            if g[v] ==-1:
                g[v] = d_next
                q.append(v)
ans = 0
for i in range(1,n+1):
    start = i*s+1
    ans += sum(g[start:start+n])
print(f"{ans/(n*n):.2f}")

```
