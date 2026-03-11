import sys; input=sys.stdin.read().split(); it=iter(input)

# 1. 初始化数据 (根据题目修改 n, m)
# u: 目标串 (Target), v: 模式串 (Pattern)
# 习惯性补空格实现 1-indexed
n = int(next(it))
u = " " + next(it)
v = " " + next(it)
m = len(v) - 1

# 2. 计算模式串 v 的 Z 数组 (a 数组)
a = [0] * (m + 1)
q, w = 0, 0
a[1] = m
for i in range(2, m + 1):
    if i <= w: a[i] = min(a[i - q + 1], w - i + 1)
    while i + a[i] <= m and v[i + a[i]] == v[1 + a[i]]: a[i] += 1
    if i + a[i] - 1 > w: q, w = i, i + a[i] - 1

# 3. 计算目标串 u 与模式串 v 的 LCP (b 数组)
b = [0] * (n + 1)
q, w = 0, 0
for i in range(1, n + 1):
    if i <= w: b[i] = min(a[i - q + 1], w - i + 1)
    while i + b[i] <= n and 1 + b[i] <= m and u[i + b[i]] == v[1 + b[i]]: b[i] += 1
    if i + b[i] - 1 > w: q, w = i, i + b[i] - 1
