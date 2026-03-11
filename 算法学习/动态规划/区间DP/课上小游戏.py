import sys

it = iter(sys.stdin.read().split())
n = int(next(it))
raw_a = [int(next(it)) for _ in range(n)]

# 1. 断环成链 (下标从1开始)
a = [0] + raw_a + raw_a
m = 2 * n

# 2. 预处理 val[i][j] (区间乘积的个位数)
val = [[0] * (m + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    val[i][i] = a[i]

for length in range(2, m + 1):
    for i in range(1, m - length + 2):      # i_max = m-length+1，右开+1
        j = i + length - 1
        val[i][j] = (val[i][j-1] * a[j]) % 10

# 3. 区间 DP
dp = [[0] * (m + 1) for _ in range(m + 1)]

for length in range(2, n + 1):              # 只需算到长度 n
    for i in range(1, m - length + 2):
        j = i + length - 1
        for k in range(i, j):               # 枚举分割点
            score = dp[i][k] + dp[k+1][j] + (val[i][k] * val[k+1][j]) // 10
            dp[i][j] = max(dp[i][j], score)

# 4. 取答案 (n 个断开位置)
ans = max(dp[i][i + n - 1] for i in range(1, n + 1))
print(ans)
