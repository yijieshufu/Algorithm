import sys

sys.setrecursionlimit(200000)

input = sys.stdin.read().split()
it = iter(input)

def get_dfs_order(n, g, root):
    L, R = [0] * (n + 1), [0] * (n + 1)
    timer, stack = 0, [(root, 0)]
    while stack:
        u, p = stack[-1]
        if L[u] == 0:
            timer += 1
            L[u] = timer
            for v in g[u]:
                if v != p: stack.append((v, u))
        else:
            R[u] = timer
            stack.pop()
    return L, R

def update(tr, i, val, n):
    while i <= n:
        tr[i] ^= val
        i += i & (-i)

def query(tr, i):
    res = 0
    while i > 0:
        res ^= tr[i]
        i -= i & (-i)
    return res

def solve():
    n, m = int(next(it)), int(next(it))

    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(next(it))

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(next(it)), int(next(it))
        g[u].append(v)
        g[v].append(u)

    L, R = get_dfs_order(n, g, 1)

    tr = [0] * (n + 1)
    for i in range(1, n + 1):
        update(tr, L[i], a[i], n)

    res = []
    for _ in range(m):
        op = next(it)
        if op == '1':
            x, y = int(next(it)), int(next(it))
            delta = a[x] ^ y
            update(tr, L[x], delta, n)
            a[x] = y
        else:
            x = int(next(it))
            ans = query(tr, R[x]) ^ query(tr, L[x] - 1)
            res.append(str(ans))

    sys.stdout.write("\n".join(res) + "\n")

solve()
