import sys
# 1. 核心 I/O 起手式
it = iter(sys.stdin.read().split())
T_cases = int(next(it))

for _ in range(T_cases):
    m, n = int(next(it)), int(next(it))
    # [块 1：地图扩边] 增加一圈海水，确保外海全连通
    g = [['0'] * (n + 2) for _ in range(m + 2)]
    for i in range(1, m + 1):
        row = next(it)
        for j in range(1, n + 1):
            g[i][j] = row[j-1]

    vis = [[False] * (n + 2) for _ in range(m + 2)]
    ans = 0
    # [块 2：外海 8 向 BFS] 从(0,0)外海出发
    q = [(0, 0)]
    vis[0][0] = True
    
    while q:
        r, c = q.pop(0)
        # 海水 8 方向渗透：关键点
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m + 2 and 0 <= nc < n + 2 and not vis[nr][nc]:
                if g[nr][nc] == '0':
                    vis[nr][nc] = True
                    q.append((nr, nc))
                else:
                    # [块 3：岛屿 4 向消解] 碰到陆地，标记整个岛屿
                    ans += 1
                    lan_q = [(nr, nc)]
                    vis[nr][nc] = True
                    while lan_q:
                        lr, lc = lan_q.pop(0)
                        for ldr, ldc in [(-1,0),(1,0),(0,-1),(0,1)]: # 岛屿仅 4 向
                            nlr, nlc = lr + ldr, lc + ldc
                            if 0 <= nlr < m + 2 and 0 <= nlc < n + 2 and not vis[nlr][nlc] and g[nlr][nlc] == '1':
                                vis[nlr][nlc] = True
                                lan_q.append((nlr, nlc))
    print(ans)