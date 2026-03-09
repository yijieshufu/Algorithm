import sys

# 【极简 I/O 起手式】
input = sys.stdin.read().split()
it = iter(input)

# ==========================================
# 【模板积木：可持久化权值线段树 (主席树内存池)】
# ==========================================
# 空间预留：N * 40 是主席树的标准安全空间
MAX_NODES = 100005 * 40
ls = [0] * MAX_NODES
rs = [0] * MAX_NODES
cnt = [0] * MAX_NODES
tot = [0] # 游标，使用列表包裹以便在函数间传递引用

def update(prev, l, r, val):
    """基于旧版本 prev，在 val 的位置插入 1 个计数，返回新版本的根节点索引"""
    tot[0] += 1
    curr = tot[0]
    # 拷贝旧节点信息（动态开点核心：只修改变化的那条链）
    ls[curr] = ls[prev]
    rs[curr] = rs[prev]
    cnt[curr] = cnt[prev] + 1

    if l == r:
        return curr

    mid = (l + r) // 2
    if val <= mid:
        ls[curr] = update(ls[prev], l, mid, val)
    else:
        rs[curr] = update(rs[prev], mid + 1, r, val)
    return curr

def query(u, v, l, r, k):
    """查询版本 v 减去版本 u 后，权值线段树中第 k 小的数值离散化索引"""
    if l == r:
        return l

    mid = (l + r) // 2
    # 左子树在区间 [l, r] 内新增的元素个数 (前缀和相减)
    num = cnt[ls[v]] - cnt[ls[u]]

    # 二分思想：左边够选就去左边，不够选就减去左边去右边
    if k <= num:
        return query(ls[u], ls[v], l, mid, k)
    else:
        return query(rs[u], rs[v], mid + 1, r, k - num)
# ==========================================


def solve():
    # 蓝桥杯 Python 必加：防止树深超过默认递归深度 1000
    sys.setrecursionlimit(200000)

    try:
        n = int(next(it))
        q = int(next(it))
    except StopIteration:
        return

    # Strictly 1-indexed
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(next(it))

    # -> 软逻辑：离散化思想。将 10^9 的数据压缩到 1~m 的稠密排名
    unique_vals = sorted(list(set(a[1:])))
    val_to_idx = {val: i + 1 for i, val in enumerate(unique_vals)}
    m = len(unique_vals) # 线段树的值域区间为 [1, m]

    # 存储 n 个版本的根节点
    root = [0] * (n + 1)

    # -> 根据题目给定的序列，从左到右逐个将离散化后的排名插入主席树，形成 n 个版本
    for i in range(1, n + 1):
        rank = val_to_idx[a[i]]
        root[i] = update(root[i-1], 1, m, rank)

    results = []
    # 处理 Q 次询问
    for _ in range(q):
        l = int(next(it))
        r = int(next(it))
        k = int(next(it))

        # -> 数据适配：根据题意特判 k=0 的情况
        if k == 0:
            results.append("1")
            continue

        # -> 核心调用：在第 r 棵树和第 l-1 棵树之间查询第 k 小，返回的是排名索引
        rank_idx = query(root[l-1], root[r], 1, m, k)

        # 映射回真实值 (rank_idx 是 1-indexed，对应数组是 0-indexed)
        real_val = unique_vals[rank_idx - 1]
        results.append(str(real_val))

    sys.stdout.write("\n".join(results) + "\n")

solve()
