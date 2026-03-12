import sys
from collections import deque

# 极简 I/O：一次性读取所有数据
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
k = int(next(it))
grid = [next(it) for _ in range(n)]

# [块 1 & 2]：初始化。c=0 表示第一拍，d=0 表示步数
q = deque([(0, 0, 0, 0)])

# [块 2]：使用 bytearray 极致节省内存，初始点标记为已访问
# 总长度为 N * M * K
vis = bytearray(n * m * k)
vis[0] = 1 

ans = -1
while q:
    r, c, cur_k, d = q.popleft()
    
    # [块 3]：到达终点立即停止
    if r == n - 1 and c == m - 1:
        ans = d
        break
        
    # 计算下一拍是什么，以及那一拍对应的目标字符
    nxt_k = (cur_k + 1) % (2 * k)
    target = 'A' if nxt_k < k else 'B'
    
    # 尝试四个方向
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        
        # 1. 越界检查 2. 字符匹配
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == target:
            # [块 2]：计算压缩后的索引 (节拍取余保证在 K 范围内)
            idx = (nr * m + nc) * k + (nxt_k % k)
            if not vis[idx]:
                vis[idx] = 1
                q.append((nr, nc, nxt_k, d + 1))

print(ans)