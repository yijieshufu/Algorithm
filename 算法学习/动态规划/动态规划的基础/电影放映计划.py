import sys

# 1. 指针式读入
d = list(map(int, sys.stdin.read().split()))
if not d: sys.exit()
p = 0

m = d[p]; p += 1  # 总时长
n = d[p]; p += 1  # 数量

a = [0] * (n + 1)
for i in range(1, n + 1):
    ti = d[p]; p += 1
    pi = d[p]; p += 1
    a[i] = (ti, pi)

k = d[p]; p += 1  # 间隔

# 2. 转换参数
m += k
f = [0] * (m + 1)

# 3. 完全背包递推
for i in range(1, n + 1):
    t, v = a[i]
    w = t + k  # 实际代价
    if w > m: continue
    for j in range(w, m + 1):
        tmp = f[j - w] + v
        if tmp > f[j]:
            f[j] = tmp

print(f[m])
