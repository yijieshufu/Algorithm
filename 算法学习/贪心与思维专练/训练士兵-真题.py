import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
s = int(next(it))
a = []
for _ in range(n):
    p = int(next(it)) # 这里的 p 是单次成本
    c = int(next(it)) # 这里的 c 是总需求次数
    a.append((c, p))
a.sort()

ans = 0
cur_k = 0
total_p = sum(x[1] for x in a)
idx = 0
while idx < n:
    c, p = a[idx]
    if total_p > s:
        # 团购逻辑：团购到让当前这个士兵满级
        if c > cur_k:
            ans += (c - cur_k) * s
            cur_k = c
        while idx < n and a[idx][0] <= cur_k:
            total_p -= a[idx][1]
            idx += 1
    else:
        if c > cur_k:
            ans += (c - cur_k) * p
        idx += 1 
print(ans)
