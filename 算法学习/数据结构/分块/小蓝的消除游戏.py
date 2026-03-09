import sys
input = sys.stdin.read().split()
it = iter(input)

n = int(next(it))
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(next(it))

q = int(next(it))
# 离线：(右端点, 左端点, 询问编号)，按 r 排序后扫右端点
queries = []
for i in range(1, q + 1):
    l, r = int(next(it)), int(next(it))
    queries.append((r, l, i))
queries.sort()

bit = [0] * (n + 1)

def update(idx, val):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

def query(idx):
    s = 0
    while idx > 0:
        s += bit[idx]
        idx -= idx & -idx
    return s

ans = [0] * (q + 1)
last = {}   # 每种颜色上次出现位置
p = 1
for r, l, idx in queries:
    # 扫描到 r：同色成对 (last[c], p) 为一块木板，在起点 last[c] 处贡献长度
    while p <= r:
        c = a[p]
        if c in last:
            update(last[c], p - last[c])
        last[c] = p
        p += 1
    # 起点在 [l, r] 内的木板长度和 = query(r) - query(l-1)
    ans[idx] = query(r) - query(l - 1)

sys.stdout.write('\n'.join(str(ans[i]) for i in range(1, q + 1)) + '\n')
