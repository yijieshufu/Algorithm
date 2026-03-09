import sys
sys.setrecursionlimit(200000)

MOD = 998244353

def mul(A, B):
    return [(A[0]*B[0]+A[1]*B[2])%MOD,(A[0]*B[1]+A[1]*B[3])%MOD,(A[2]*B[0]+A[3]*B[2])%MOD,(A[2]*B[1]+A[3]*B[3])%MOD]

def build(u, l, r, A, t):
    if l == r: t[u] = A[l]; return
    m = (l + r) // 2
    build(u*2, l, m, A, t); build(u*2+1, m+1, r, A, t)
    t[u] = mul(t[u*2], t[u*2+1])

def upd(u, l, r, i, D, t):
    if l == r: t[u] = D; return
    m = (l + r) // 2
    upd(u*2, l, m, i, D, t) if i <= m else upd(u*2+1, m+1, r, i, D, t)
    t[u] = mul(t[u*2], t[u*2+1])

def qry(u, l, r, ql, qr, t):
    if ql <= l and r <= qr: return t[u]
    m = (l + r) // 2
    if qr <= m: return qry(u*2, l, m, ql, qr, t)
    if ql > m: return qry(u*2+1, m+1, r, ql, qr, t)
    return mul(qry(u*2, l, m, ql, qr, t), qry(u*2+1, m+1, r, ql, qr, t))

data = sys.stdin.read().split()
if not data: exit()
it = iter(data)
n, q = int(next(it)), int(next(it))
A = [[1,0,0,1]] + [[int(next(it)) for _ in range(4)] for _ in range(n)]
tree = [None] * (4 * n + 1)
build(1, 1, n, A, tree)
for _ in range(q):
    op = int(next(it))
    if op == 1:
        upd(1, 1, n, int(next(it)), [int(next(it)) for _ in range(4)], tree)
    else:
        print(*qry(1, 1, n, int(next(it)), int(next(it)), tree))
