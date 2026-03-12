import sys

# --- 块 1：最高效输入与环境初始化 ---
input_data = sys.stdin.read().split()
it = iter(input_data)
n = int(next(it))
m = int(next(it))

# 一维平铺：stride 为行跨度，多加 2 列作为哨兵边界
stride = n + 2
size = stride * stride
dist = [-1] * size

# 设置哨兵边界：外围一圈初始化为 -2（代表不可访问）
for i in range(stride):
    dist[i] = -2                    # 第一行
    dist[size - stride + i] = -2    # 最后一行
    dist[i * stride] = -2           # 第一列
    dist[i * stride + n + 1] = -2   # 最后一列

# --- 块 2：传送门预处理 ---
portals = [[] for _ in range(size)]
has_p = [0] * size  # 标记位，用于加速判断 标记此地有“暗道”
for _ in range(m):
    r1, c1, r2, c2 = int(next(it)), int(next(it)), int(next(it)), int(next(it))
    u = r1 * stride + c1
    v = r2 * stride + c2
    portals[u].append(v)
    portals[v].append(u)
    has_p[u] = 1
    has_p[v] = 1

# --- 块 3：单源 BFS 过程 ---
# 从终点 (n, n) 开始反向搜索
target = n * stride + n
dist[target] = 0
q = [target]
head = 0

# 预存移动偏移量：右, 左, 下, 上
offs = [1, -1, stride, -stride]

while head < len(q):
    u = q[head]
    head += 1
    d_next = dist[u] + 1
    
    # 1. 尝试四向移动
    for o in offs:
        v = u + o
        if dist[v] == -1:  # 利用哨兵，一步判断越界和访问情况
            dist[v] = d_next
            q.append(v)
    
    # 2. 尝试传送门移动 (仅当当前点有传送门时执行)
    if has_p[u]:
        for v in portals[u]:
            if dist[v] == -1:
                dist[v] = d_next
                q.append(v)

# --- 块 4：汇总结果 ---
total = 0
for r in range(1, n + 1):
    row_start = r * stride
    for c in range(1, n + 1):
        total += dist[row_start + c]

print("{:.2f}".format(total / (n * n)))