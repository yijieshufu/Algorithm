# AB路线
- **地图**：$N \times M$ 的网格，填充字母 'A' 或 'B'。
- **规则**：必须先走 $K$ 个 A，再走 $K$ 个 B，再走 $K$ 个 A... 如此循环。
- **注意**：最后一段可以不走满 $K$ 个。起点保证是 A。
- **目标**：从 $(0,0)$ 到 $(N-1, M-1)$ 的最少步数。若无法到达输出 -1。
# 分析
由于移动取决于当前的“节奏”，我们的 BFS 状态必须包含**节奏进度**。
- **状态表示**：$(r, c, \text{cur\_k})$。
    - $(r, c)$：当前坐标。
    - $\text{cur\_k}$：当前处于 $2K$ 周期中的第几拍（$0 \le \text{cur\_k} < 2K$）。
- **判定逻辑**：
    - 若下一拍 $1 \le \text{nxt\_k} \le K$，目标格必须是 'A'。
    - 若下一拍 $K+1 \le \text{nxt\_k} \le 2K$（或 $0$），目标格必须是 'B'。
# 代码
```python
import sys
from collections import deque
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
k = int(next(it))
grid = [next(it) for _ in range(n)]
q = deque([(0, 0, 0, 0)])
vis = bytearray(n * m * k)
vis[0] = 1 
ans = -1
while q:
    r, c, cur_k, d = q.popleft()
    if r == n - 1 and c == m - 1:
        ans = d
        break
    nxt_k = (cur_k + 1) % (2 * k)
    target = 'A' if nxt_k < k else 'B'
    # 尝试四个方向
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == target:
            idx = (nr * m + nc) * k + (nxt_k % k)
            if not vis[idx]:
                vis[idx] = 1
                q.append((nr, nc, nxt_k, d + 1))

print(ans)
```