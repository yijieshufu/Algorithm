import sys
import math
# [起手式：标准 I/O 与数据打包]
it = iter(sys.stdin.read().split())
n = int(next(it))
# a: 存储圆信息 (x, y, r)
a = [(int(next(it)), int(next(it)), int(next(it))) for _ in range(n)]
# [块 1：状态定义]
f = [1e18] * n  # lowcost 数组，记录到生成树的最短距离
f[0] = 0.0
q = list(range(n)) # 未访问集合 (unvisited)
ans = 0.0
sq = math.sqrt # 局部化函数提速
while q:
    # 1. 寻找当前 f 值最小的点 u (变量 p 为索引，u 为节点编号)
    p = 0
    for i in range(1, len(q)):
        if f[q[i]] < f[q[p]]: 
            p = i
    u = q[p]
    ans += f[u]
    # [块 2：O(1) 极速斩杀 - 覆盖并弹出]
    q[p] = q[-1]
    q.pop()
    # 2. 更新剩余点到生成树的距离
    ux, uy, ur = a[u]
    for v in q:
        vx, vy, vr = a[v]
        # [块 3：算术降级 - 避免 **2]
        dx, dy = ux - vx, uy - vy
        d2 = dx * dx + dy * dy
        sr = ur + vr
        # 几何判定：若平方和 <= 半径和平方，则相交代价为 0
        c = 0.0 if d2 <= sr * sr else sq(d2) - sr
        if c < f[v]: 
            f[v] = c
print(f"{ans:.2f}")