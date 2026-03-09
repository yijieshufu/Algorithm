import sys
sys.setrecursionlimit(200000)
input = sys.stdin.read().split()
it = iter(input)
n, m = int(next(it)), int(next(it))
N = n + 2
f = [0] * (N + 1); lc = [0] * (N + 1); rc = [0] * (N + 1); s = [0] * (N + 1); rv = [0] * (N + 1); v = [0] * (N + 1)
rt = 0

def up(x): s[x] = s[lc[x]] + s[rc[x]] + 1

def dn(x):
    if rv[x]:
        lc[x], rc[x] = rc[x], lc[x]
        if lc[x]: rv[lc[x]] ^= 1
        if rc[x]: rv[rc[x]] ^= 1
        rv[x] = 0

def rot(x):
    y, z = f[x], f[y]
    if lc[y] == x: lc[y] = rc[x]; (rc[x] and f.__setitem__(rc[x], y)); rc[x] = y
    else: rc[y] = lc[x]; (lc[x] and f.__setitem__(lc[x], y)); lc[x] = y
    f[y], f[x] = x, z
    if z: lc[z], rc[z] = (x, rc[z]) if lc[z] == y else (lc[z], x)
    up(y); up(x)

def spl(x, g):
    while f[x] != g:
        y, z = f[x], f[y]
        if z != g: rot(y if (lc[y] == x) == (lc[z] == y) else x)
        rot(x)
    if not g: global rt; rt = x

def kth(k):
    u = rt
    while 1:
        dn(u)
        if s[lc[u]] >= k: u = lc[u]
        elif s[lc[u]] + 1 == k: return u
        else: k -= s[lc[u]] + 1; u = rc[u]

def bld(l, r, p):
    if l > r: return 0
    mid = (l + r) // 2
    v[mid], f[mid] = mid, p
    lc[mid] = bld(l, mid - 1, mid); rc[mid] = bld(mid + 1, r, mid)
    up(mid); return mid

rt = bld(1, N, 0)
for _ in range(m):
    l, r = int(next(it)), int(next(it))
    L, R = kth(l), kth(r + 2)
    spl(L, 0); spl(R, L)
    rv[lc[R]] ^= 1

res = []; stack = []; curr = rt
while stack or curr:
    if curr: dn(curr); stack.append(curr); curr = lc[curr]
    else:
        curr = stack.pop()
        if 1 < v[curr] < N: res.append(str(v[curr] - 1))
        curr = rc[curr]
sys.stdout.write(" ".join(res) + "\n")
