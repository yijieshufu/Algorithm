import sys
from collections import deque

# 1. 极简 I/O 起手式
it = iter(sys.stdin.read().split())
n, m = int(next(it)), int(next(it))
g = [[int(next(it)) for _ in range(m)] for _ in range(n)]
# 坐标转 0-indexed [块 1]
x1, y1 = int(next(it))-1, int(next(it))-1
x2, y2 = int(next(it))-1, int(next(it))-1

# 2. 核心状态定义 [块 1]
dist = [[-1] * m for _ in range(n)]
q = deque([(x1, y1)])
dist[x1][y1] = 0
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
ans = -1

# 3. BFS 主循环 [块 2, 3]
while q:
    r, c = q.popleft()
    if r == x2 and c == y2:
        ans = dist[r][c]
        break
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        # 边界与合法性检查 [块 3]
        if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == 1 and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

print(ans)