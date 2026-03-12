import sys

# 认知块 1: 高效输入流
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]

# 认知块 1: 预处理前缀异或和 (包含 S[0]=0)
s = [0] * (n + 1)
for i in range(n):
    s[i+1] = s[i] ^ a[i]
ans = 0
# 认知块 2: 按位拆分 (A_i < 2^20)
for k in range(21):
    cnt0 = 0
    cnt1 = 0
    # 认知块 3: 统计当前位 0 和 1 的分布
    for x in s:
        if (x >> k) & 1:
            cnt1 += 1
        else:
            cnt0 += 1
    # 乘法原理计算贡献并累加
    ans += (cnt0 * cnt1) * (1 << k)
print(ans)