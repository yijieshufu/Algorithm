import sys
input = sys.stdin.read().split()
it = iter(input)
sys.setrecursionlimit(200000)

def hld_init(n, g, root):
    sz, dep, fa, son = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
    stack, order = [(root, 0, 1)], []
    while stack:
        u, p, d = stack.pop()
        fa[u], dep[u], sz[u] = p, d, 1
        order.append(u)
        for v, w in g[u]:
            if v != p: stack.append((v, u, d+1))
    for u in reversed(order):
        if fa[u]:
            sz[fa[u]] += sz[u]
            if son[fa[u]] == 0 or sz[u] > sz[son[fa[u]]]: son[fa[u]] = u
    top, dfn, rnk, cur_dfn = [0]*(n+1), [0]*(n+1), [0]*(n+1), 0
    stack = [(root, root)]
    while stack:
        u, t = stack.pop()
        cur_dfn += 1
        dfn[u], rnk[cur_dfn], top[u] = cur_dfn, u, t
        for v, w in g[u]:
            if v != fa[u] and v != son[u]: stack.append((v, v))
        if son[u]: stack.append((son[u], t))
    return dfn, rnk, top, fa, dep

def build(node, l, r, rnk, a, tree):
    if l == r:
        tree[node] = a[rnk[l]]
        return
    mid = (l + r) // 2
    build(node * 2, l, mid, rnk, a, tree)
    build(node * 2 + 1, mid + 1, r, rnk, a, tree)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

def push_down(node, l, r, tree, lazy):
    if lazy[node] != 0:
        mid, v = (l + r) // 2, lazy[node]
        if (mid - l + 1) % 2: tree[node * 2] ^= v
        lazy[node * 2] ^= v
        if (r - mid) % 2: tree[node * 2 + 1] ^= v
        lazy[node * 2 + 1] ^= v
        lazy[node] = 0

def update(node, l, r, ql, qr, val, tree, lazy):
    if ql <= l and r <= qr:
        if (r - l + 1) % 2: tree[node] ^= val
        lazy[node] ^= val
        return
    push_down(node, l, r, tree, lazy)
    mid = (l + r) // 2
    if ql <= mid: update(node * 2, l, mid, ql, qr, val, tree, lazy)
    if qr > mid: update(node * 2 + 1, mid + 1, r, ql, qr, val, tree, lazy)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

def query(node, l, r, ql, qr, tree, lazy):
    if ql <= l and r <= qr: return tree[node]
    push_down(node, l, r, tree, lazy)
    mid = (l + r) // 2
    res = 0
    if ql <= mid: res ^= query(node * 2, l, mid, ql, qr, tree, lazy)
    if qr > mid: res ^= query(node * 2 + 1, mid + 1, r, ql, qr, tree, lazy)
    return res

def solve():
    n = int(next(it))
    q = int(next(it))
    w = [0] + [int(next(it)) for _ in range(n)]
    g = [[] for _ in range(n + 1)]
    adj_edge_xor = [0] * (n + 1)

    for _ in range(n - 1):
        u, v, c = int(next(it)), int(next(it)), int(next(it))
        g[u].append((v, c))
        g[v].append((u, c))
        adj_edge_xor[u] ^= c
        adj_edge_xor[v] ^= c

    dfn, rnk, top, fa, dep = hld_init(n, g, 1)
    tree, lazy = [0] * (4 * n + 1), [0] * (4 * n + 1)
    build(1, 1, n, rnk, w, tree)

    for _ in range(q):
        op = int(next(it))
        if op == 1:
            a, b, x = int(next(it)), int(next(it)), int(next(it))
            adj_edge_xor[a] ^= x
            adj_edge_xor[b] ^= x
        elif op == 2:
            a, b, x = int(next(it)), int(next(it)), int(next(it))
            while top[a] != top[b]:
                if dep[top[a]] < dep[top[b]]: a, b = b, a
                update(1, 1, n, dfn[top[a]], dfn[a], x, tree, lazy)
                a = fa[top[a]]
            if dep[a] > dep[b]: a, b = b, a
            update(1, 1, n, dfn[a], dfn[b], x, tree, lazy)
        elif op == 3:
            a, b = int(next(it)), int(next(it))
            res = 0
            while top[a] != top[b]:
                if dep[top[a]] < dep[top[b]]: a, b = b, a
                res ^= query(1, 1, n, dfn[top[a]], dfn[a], tree, lazy)
                a = fa[top[a]]
            if dep[a] > dep[b]: a, b = b, a
            res ^= query(1, 1, n, dfn[a], dfn[b], tree, lazy)
            print(res)
        elif op == 4:
            a = int(next(it))
            cur_w = query(1, 1, n, dfn[a], dfn[a], tree, lazy)
            print(cur_w ^ adj_edge_xor[a])

solve()
