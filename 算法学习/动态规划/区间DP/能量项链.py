def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # 破环成链
    a = a + a
    m = 2 * n
    
    # 初始化
    dp = [[0] * m for _ in range(m)]
    
    # 区间DP：按长度从小到大枚举
    for length in range(2, n + 1):          # 区间长度（珠子个数）
        for i in range(m - length + 1):     # 起点（防越界：i + length - 1 < m）
            j = i + length - 1               # 终点
            for k in range(i, j):            # 枚举分割点
                dp[i][j] = max(dp[i][j], 
                    dp[i][k] + dp[k+1][j] + a[i] * a[k+1] * a[j+1])
    
    # 环形：找长度为n的区间最大值
    ans = max(dp[i][i+n-1] for i in range(n))
    print(ans)

solve()
