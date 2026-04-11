# AB路线
**输入**：网格大小 $N, M$，周期参数 $K$。  
**地图**：只包含 `'A'` 和 `'B'` 的网格。起点固定为 `'A'`。  
**规则**：走 $K$ 步 `'A'`，走 $K$ 步 `'B'`，如此无限交替（最后一段可不走满）。  
**目标**：从 $(0,0)$ 移动到 $(N-1, M-1)$ 的最少步数。不可达输出 `-1`。
# 分析
**核心解法：扩维 BFS**
- **周期映射**：将 $2K$ 视为一个完整周期 `k2 = 2 * k`。下一步的索引是 `nk = (d + 1) % k2`。
    - 若 `nk < k`，目标格必须是 `'A'`。
    - 若 `nk >= k`，目标格必须是 `'B'`。
- **状态去重**：必须使用一维展开的 `v[u * k2 + nk]` 来去重。
- **空间哨兵**：给网格加一圈外框 `'X'`，一维化后跨度为 $s = M + 2$。
# 代码
```python
import sys

it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
k = int(next(it))
# 哨兵填充 + 一维平铺
s = m + 2
g = ['X'] * ((n + 2) * s)
for i in range(1, n + 1):
    g[i * s + 1 : i * s + m + 1] = list(next(it))
k2 = 2 * k
v = [0] * (len(g) * k2)

start = s + 1
target = n * s + m

q = [(start, 0)]
h = 0
v[start * k2] = 1 

ans = -1
while h < len(q):
    u, d = q[h]
    h += 1
    
    if u == target:
        ans = d
        break
        
    nd = d + 1
    nk = nd % k2
    tc = 'A' if nk < k else 'B'
    
    # 游走与状态转移
    for o in (1, -1, s, -s):
        nu = u + o
        if g[nu] == tc:
            idx = nu * k2 + nk
            if not v[idx]:
                v[idx] = 1
                q.append((nu, nd))

print(ans)
```