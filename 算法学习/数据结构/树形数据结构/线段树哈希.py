import sys
it = iter(sys.stdin.read().split())
n, q = int(next(it)), int(next(it))
s_str = next(it)
mod = 1000000007
p = 131

s = [0] + [ord(s_str[i]) for i in range(n)]
powP = [1] * (n + 1)
for i in range(1, n + 1):
    powP[i] = powP[i - 1] * p % mod

def upd(i, d, bit):
    while i <= n: bit[i] = (bit[i] + d) % mod; i += i & -i

def qry(i, bit):
    r = 0
    while i > 0: r = (r + bit[i]) % mod; i -= i & -i
    return r

bit = [0] * (n + 1)
for i in range(1, n + 1):
    upd(i, s[i] * powP[i - 1] % mod, bit)

for _ in range(q):
    op = int(next(it))
    if op == 1:
        x, c = int(next(it)), next(it)
        d = (ord(c) - s[x]) * powP[x - 1] % mod
        upd(x, d, bit)
        s[x] = ord(c)
    else:
        l1, r1, l2, r2 = int(next(it)), int(next(it)), int(next(it)), int(next(it))
        if r1 - l1 != r2 - l2:
            print("No")
            continue
        h1 = (qry(r1, bit) - qry(l1 - 1, bit) + mod) % mod
        h2 = (qry(r2, bit) - qry(l2 - 1, bit) + mod) % mod
        if l1 < l2: h1 = h1 * powP[l2 - l1] % mod
        else: h2 = h2 * powP[l1 - l2] % mod
        print("Yes" if h1 == h2 else "No")
