import sys
sys.setrecursionlimit(1_000_000)

it = iter(sys.stdin.read().split())

n, q = int(next(it)), int(next(it))


MAX_N = 200005 * 40
ls, rs, cnt = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N
root, tot = [0] * 200005, 0

def upd(prev, l, r, pos):
    global tot
    tot += 1
    curr = tot
    ls[curr], rs[curr], cnt[curr] = ls[prev], rs[prev], cnt[prev] + 1
    if l == r: return curr
    mid = (l + r) // 2
    if pos <= mid: ls[curr] = upd(ls[prev], l, mid, pos)
    else: rs[curr] = upd(rs[prev], mid + 1, r, pos)
    return curr

def qry(u, v, l, r, k):
    if l == r: return l
    mid = (l + r) // 2
    num = cnt[ls[v]] - cnt[ls[u]]
    return qry(ls[u], ls[v], l, mid, k) if k <= num else qry(rs[u], rs[v], mid + 1, r, k - num)

a = [0] + [int(next(it)) for _ in range(n)]
u = sorted(set(a[1:]))
rank = {v: i + 1 for i, v in enumerate(u)}
m = len(u)
for i in range(1, n + 1):
    root[i] = upd(root[i - 1], 1, m, rank[a[i]])

out = []
for _ in range(q):
    l, r, k = int(next(it)), int(next(it)), int(next(it))
    idx = qry(root[l - 1], root[r], 1, m, k)
    out.append(str(u[idx - 1]))
print("\n".join(out))
