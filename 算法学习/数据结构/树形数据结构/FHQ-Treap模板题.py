import sys, random
sys.setrecursionlimit(200000)

input = sys.stdin.read().split()
it = iter(input)

n, m = int(next(it)), int(next(it))

# ls/rs: 左右儿子, sz: 子树大小, val: 节点值, rnd: 优先级, tag: 翻转标记
ls, rs, sz, tag = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
val = [i for i in range(n+1)]
rnd = [random.random() for _ in range(n+1)]

for i in range(1, n+1): sz[i] = 1

def up(u):
    sz[u] = sz[ls[u]] + sz[rs[u]] + 1

def down(u):
    if u and tag[u]:
        ls[u], rs[u] = rs[u], ls[u]
        if ls[u]: tag[ls[u]] ^= 1
        if rs[u]: tag[rs[u]] ^= 1
        tag[u] = 0

def split(u, k):
    if not u: return 0, 0
    down(u)
    if sz[ls[u]] >= k:
        l, r = split(ls[u], k)
        ls[u] = r; up(u)
        return l, u
    else:
        l, r = split(rs[u], k - sz[ls[u]] - 1)
        rs[u] = l; up(u)
        return u, r

def merge(u, v):
    if not u or not v: return u + v
    down(u); down(v)
    if rnd[u] < rnd[v]:
        rs[u] = merge(rs[u], v); up(u)
        return u
    else:
        ls[v] = merge(u, ls[v]); up(v)
        return v

root = 0
for i in range(1, n+1): root = merge(root, i)

for _ in range(m):
    L, R = int(next(it)), int(next(it))
    t1, t3 = split(root, R)
    t1, t2 = split(t1, L-1)
    if t2: tag[t2] ^= 1
    root = merge(merge(t1, t2), t3)

ans = []
def get_ans(u):
    if not u: return
    down(u)
    get_ans(ls[u])
    ans.append(str(val[u]))
    get_ans(rs[u])

get_ans(root)
sys.stdout.write(" ".join(ans) + "\n")