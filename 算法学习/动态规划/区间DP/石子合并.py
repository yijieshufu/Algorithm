import sys

# 快速输入
input = sys.stdin.readline

def solve():
    n = int(input())
    # 下标从1开始，方便处理
    a = [0] + list(map(int, input().split()))
    
    # 前缀和：s[i] = a[1] + ... + a[i]
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
    
    # dp[i][j]：合并区间[i,j]的最小代价
    # 初始化：dp[i][i] = 0（单堆无需合并），其他为无穷大
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            dp[i][j] = float('inf')
    
    # 区间DP：按长度从小到大枚举
    for length in range(2, n + 1):           # 区间长度
        for i in range(1, n - length + 2):   # 起点i
            j = i + length - 1                # 终点j
            # 枚举分割点k：i ≤ k < j
            for k in range(i, j):
                # 左区间[i,k] + 右区间[k+1,j] + 合并代价
                cost = dp[i][k] + dp[k + 1][j] + s[j] - s[i - 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    print(dp[1][n])

if __name__ == "__main__":
    solve()
