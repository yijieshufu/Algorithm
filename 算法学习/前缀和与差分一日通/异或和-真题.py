import sys
# 1. 快速读入
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [0] + [int(next(it)) for _ in range(n)] # 1-indexed 方便对应下标 j
ans = 0
# 2. 核心推导：按位统计贡献
for k in range(31):
    c0, s0 = 0, 0  # 块 3：初始化当前位的状态
    c1, s1 = 0, 0
    bit_total = 0
    for j in range(1, n + 1):
        if (a[j] >> k) & 1:
            # 块 2：当前位是 1，找之前所有位是 0 的 i
            bit_total += (j * c0 - s0)
            c1 += 1
            s1 += j
        else:
            # 块 2：当前位是 0，找之前所有位是 1 的 i
            bit_total += (j * c1 - s1)
            c0 += 1
            s0 += j
    ans += bit_total * (1 << k) # 累加到总答案
print(ans)