import sys

input_data = sys.stdin.read().split()
it = iter(input_data)

def hld_init(n, g, root):
    sz = [0] * (n + 1)
    dep = [0] * (n + 1)
    fa = [0] * (n + 1)
    son = [0] * (n + 1)

    stack = [(root, 0, 1)]
    order = []
    while stack:
        u, p, d = stack.pop()
        fa[u] = p
        dep[u] = d
        sz[u] = 1
        order.append(u)
        for v in g[u]:
            if v != p:
                stack.append((v, u, d + 1))

    for u in reversed(order):
        if fa[u]:
            sz[fa[u]] += sz[u]
            if son[fa[u]] == 0 or sz[u] > sz[son[fa[u]]]:
                son[fa[u]] = u

    top = [0] * (n + 1)
    dfn = [0] * (n + 1)
    rnk = [0] * (n + 1)
    cur_dfn = 0

    stack = [(root, root)]
    while stack:
        u, t = stack.pop()
        cur_dfn += 1
        dfn[u] = cur_dfn
        rnk[cur_dfn] = u
        top[u] = t

        for v in g[u]:
            if v != fa[u] and v != son[u]:
                stack.append((v, v))
        if son[u]:
            stack.append((son[u], t))

    return dfn, rnk, top, fa, dep, sz

def build(node, l, r, rnk, a, tree):
    if l == r:
        tree[node] = a[rnk[l]]
        return
    mid = (l + r) // 2
    build(node * 2, l, mid, rnk, a, tree)
    build(node * 2 + 1, mid + 1, r, rnk, a, tree)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def push_down(node, l, r, tree, lazy):
    if lazy[node] != 0:
        mid = (l + r) // 2
        lazy[node * 2] += lazy[node]
        tree[node * 2] += lazy[node] * (mid - l + 1)
        lazy[node * 2 + 1] += lazy[node]
        tree[node * 2 + 1] += lazy[node] * (r - mid)
        lazy[node] = 0

def update(node, l, r, ql, qr, val, tree, lazy):
    if ql <= l and r <= qr:
        tree[node] += val * (r - l + 1)
        lazy[node] += val
        return
    push_down(node, l, r, tree, lazy)
    mid = (l + r) // 2
    if ql <= mid: update(node * 2, l, mid, ql, qr, val, tree, lazy)
    if qr > mid: update(node * 2 + 1, mid + 1, r, ql, qr, val, tree, lazy)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, l, r, ql, qr, tree, lazy):
    if ql <= l and r <= qr:
        return tree[node]
    push_down(node, l, r, tree, lazy)
    mid = (l + r) // 2
    res = 0
    if ql <= mid: res += query(node * 2, l, mid, ql, qr, tree, lazy)
    if qr > mid: res += query(node * 2 + 1, mid + 1, r, ql, qr, tree, lazy)
    return res

def solve():
    n = int(next(it))

    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(next(it))

    g = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        f = int(next(it))
        g[f].append(i)
        g[i].append(f)

    m = int(next(it))

    dfn, rnk, top, fa, dep, sz = hld_init(n, g, 1)

    tree = [0] * (4 * n + 1)
    lazy = [0] * (4 * n + 1)
    build(1, 1, n, rnk, a, tree)

    cur_root = 1

    def get_child_toward(u, rt):
        curr = rt
        while top[curr] != top[u]:
            if fa[top[curr]] == u:
                return top[curr]
            curr = fa[top[curr]]
        return rnk[dfn[u] + 1]

    for _ in range(m):
        op = int(next(it))
        if op == 1:
            cur_root = int(next(it))

        elif op == 2:
            u, v, k = int(next(it)), int(next(it)), int(next(it))
            while top[u] != top[v]:
                if dep[top[u]] < dep[top[v]]: u, v = v, u
                update(1, 1, n, dfn[top[u]], dfn[u], k, tree, lazy)
                u = fa[top[u]]
            if dep[u] > dep[v]: u, v = v, u
            update(1, 1, n, dfn[u], dfn[v], k, tree, lazy)

        elif op == 3:
            u, k = int(next(it)), int(next(it))
            if u == cur_root:
                update(1, 1, n, 1, n, k, tree, lazy)
            elif dfn[cur_root] >= dfn[u] and dfn[cur_root] <= dfn[u] + sz[u] - 1:
                child = get_child_toward(u, cur_root)
                if dfn[child] > 1:
                    update(1, 1, n, 1, dfn[child] - 1, k, tree, lazy)
                if dfn[child] + sz[child] <= n:
                    update(1, 1, n, dfn[child] + sz[child], n, k, tree, lazy)
            else:
                update(1, 1, n, dfn[u], dfn[u] + sz[u] - 1, k, tree, lazy)

        elif op == 4:
            u, v = int(next(it)), int(next(it))
            res = 0
            while top[u] != top[v]:
                if dep[top[u]] < dep[top[v]]: u, v = v, u
                res += query(1, 1, n, dfn[top[u]], dfn[u], tree, lazy)
                u = fa[top[u]]
            if dep[u] > dep[v]: u, v = v, u
            res += query(1, 1, n, dfn[u], dfn[v], tree, lazy)
            print(res)

        elif op == 5:
            u = int(next(it))
            if u == cur_root:
                print(query(1, 1, n, 1, n, tree, lazy))
            elif dfn[cur_root] >= dfn[u] and dfn[cur_root] <= dfn[u] + sz[u] - 1:
                child = get_child_toward(u, cur_root)
                res = 0
                if dfn[child] > 1:
                    res += query(1, 1, n, 1, dfn[child] - 1, tree, lazy)
                if dfn[child] + sz[child] <= n:
                    res += query(1, 1, n, dfn[child] + sz[child], n, tree, lazy)
                print(res)
            else:
                print(query(1, 1, n, dfn[u], dfn[u] + sz[u] - 1, tree, lazy))

solve()
