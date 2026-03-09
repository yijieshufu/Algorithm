import sys

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
it = iter(input_data)

def build_tree(n, edges):
    g = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for u, v in edges:
        g[u].append(v)
        deg[v] += 1

    root = 1
    for i in range(1, n + 1):
        if deg[i] == 0:
            root = i
            break
    return g, root

def dfs_subtree(u, g, val, res):
    res[u] = val[u]
    for v in g[u]:
        dfs_subtree(v, g, val, res)
        res[u] += res[v]

def solve():
    n = int(next(it))

    val = [0] * (n + 1)
    for i in range(1, n + 1):
        val[i] = int(next(it))

    edges = []
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))

    g, root = build_tree(n, edges)

    res = [0] * (n + 1)
    dfs_subtree(root, g, val, res)

    q_str = next(it)
    q = int(q_str)
    ans = []
    for _ in range(q):
        x = int(next(it))
        ans.append(str(res[x]))

    sys.stdout.write("\n".join(ans) + "\n")

solve()
