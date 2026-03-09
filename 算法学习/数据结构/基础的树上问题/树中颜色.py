import sys

sys.setrecursionlimit(200000)
input = sys.stdin.read().split()
it = iter(input)

def build_tree(n, edges):
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g

def count_bits(mask):
    return bin(mask).count('1')

def solve():
    n = int(next(it))
    q = int(next(it))

    colors = [0] * (n + 1)
    for i in range(1, n + 1):
        colors[i] = int(next(it))

    edges = []
    for _ in range(n - 1):
        u, v = int(next(it)), int(next(it))
        edges.append((u, v))
    g = build_tree(n, edges)

    subtree_mask = [0] * (n + 1)

    def dfs(u, p):
        curr_mask = 1 << colors[u]
        for v in g[u]:
            if v != p:
                curr_mask |= dfs(v, u)
        subtree_mask[u] = curr_mask
        return curr_mask

    dfs(1, 0)

    results = []
    for _ in range(q):
        x = int(next(it))
        results.append(str(count_bits(subtree_mask[x])))

    sys.stdout.write("\n".join(results) + "\n")

solve()
