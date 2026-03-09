import sys
from bisect import bisect_left

it = iter(sys.stdin.read().split())
q_str = next(it, None)
if q_str is None: exit()
q = int(q_str)

ops, all_vals = [], []
for _ in range(q):
    t = int(next(it))
    if t == 1:
        x, c = int(next(it)), int(next(it))
        ops.append((1, x, c)); all_vals.append(c)
    else:
        c = int(next(it))
        ops.append((2, c)); all_vals.append(c)

uc = sorted(set(all_vals))
n, tree = len(uc), [0] * (len(uc) + 1)

def upd(i, d):
    while i <= n: tree[i] += d; i += i & -i

def qry(i):
    s = 0
    while i > 0: s += tree[i]; i -= i & -i
    return s

res = []
for op in ops:
    idx = bisect_left(uc, op[2] if op[0] == 1 else op[1]) + 1
    if op[0] == 1:
        upd(idx, op[1] * op[2])
    else:
        res.append(str(qry(idx)))
print('\n'.join(res))
