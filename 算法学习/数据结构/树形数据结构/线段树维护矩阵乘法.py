import sys
sys.setrecursionlimit(200000)

it = iter(sys.stdin.read().split())
mod = 1000000007
n, q = int(next(it)), int(next(it))
a_init = [0] + [int(next(it)) for _ in range(n)]

def mat_pow(k):
    a, b, c, d = 1, 1, 1, 0
    ra, rb, rc, rd = 1, 0, 0, 1
    while k:
        if k & 1:
            ra, rb, rc, rd = (ra*a+rb*c)%mod,(ra*b+rb*d)%mod,(rc*a+rd*c)%mod,(rc*b+rd*d)%mod
        ta, tb, tc, td = (a*a+b*c)%mod,(a*b+b*d)%mod,(c*a+d*c)%mod,(c*b+d*d)%mod
        a, b, c, d = ta, tb, tc, td
        k >>= 1
    return ra, rb, rc, rd

t_v1 = [0] * (4 * n + 1)
t_v2 = [0] * (4 * n + 1)
la = [1] * (4 * n + 1)
lb = [0] * (4 * n + 1)
lc = [0] * (4 * n + 1)
ld = [1] * (4 * n + 1)

def apply(p, ma, mb, mc, md):
    # 矩阵 [ma,mb; mc,md] 左乘当前节点向量 (t_v1, t_v2)
    t_v1[p], t_v2[p] = (ma*t_v1[p]+mb*t_v2[p])%mod, (mc*t_v1[p]+md*t_v2[p])%mod
    # 懒标记合并：新矩阵左乘旧懒标记矩阵
    la[p], lb[p], lc[p], ld[p] = (ma*la[p]+mb*lc[p])%mod,(ma*lb[p]+mb*ld[p])%mod,(mc*la[p]+md*lc[p])%mod,(mc*lb[p]+md*ld[p])%mod

def push_down(p):
    if (la[p], lb[p], lc[p], ld[p]) == (1, 0, 0, 1): return
    l, r = p << 1, p << 1 | 1
    apply(l, la[p], lb[p], lc[p], ld[p]); apply(r, la[p], lb[p], lc[p], ld[p])
    la[p], lb[p], lc[p], ld[p] = 1, 0, 0, 1

def push_up(p):
    t_v1[p] = (t_v1[p<<1] + t_v1[p<<1|1]) % mod
    t_v2[p] = (t_v2[p<<1] + t_v2[p<<1|1]) % mod

def build(p, l, r):
    if l == r:
        ma, mb, mc, md = mat_pow(a_init[l])
        t_v1[p], t_v2[p] = ma, mc
        return
    m = (l + r) // 2
    build(p << 1, l, m); build(p << 1 | 1, m + 1, r)
    push_up(p)

def upd(p, l, r, ql, qr, ma, mb, mc, md):
    if ql <= l and r <= qr: apply(p, ma, mb, mc, md); return
    push_down(p)
    m = (l + r) // 2
    if ql <= m: upd(p << 1, l, m, ql, qr, ma, mb, mc, md)
    if qr > m: upd(p << 1 | 1, m + 1, r, ql, qr, ma, mb, mc, md)
    push_up(p)

def qry(p, l, r, ql, qr):
    if ql <= l and r <= qr: return t_v2[p]
    push_down(p)
    m = (l + r) // 2
    res = 0
    if ql <= m: res = (res + qry(p << 1, l, m, ql, qr)) % mod
    if qr > m: res = (res + qry(p << 1 | 1, m + 1, r, ql, qr)) % mod
    return res

build(1, 1, n)
for _ in range(q):
    op = int(next(it))
    if op == 1:
        l, r, x = int(next(it)), int(next(it)), int(next(it))
        upd(1, 1, n, l, r, *mat_pow(x))
    else:
        print(qry(1, 1, n, int(next(it)), int(next(it))))
