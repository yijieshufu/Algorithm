import sys

def solve():
    # 极速 IO 读取
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    n = int(next(it))
    # a[i] 表示位置 i 骰子的最大点数
    a = [0] + [int(next(it)) for _ in range(n - 1)]
    
    MOD = 998244353
    
    # dp[i]: 到达终点的期望步数
    dp = [0] * (n + 2)
    # suffix[i]: dp 数组的后缀和
    suffix = [0] * (n + 2)
    
    # 倒序遍历（从 n-1 回到 1）
    for i in range(n - 1, 0, -1):
        ai = a[i]
        
        # 1. 计算区间和 [i+1, i+ai]
        # 公式: S[L] - S[R+1]
        range_sum = (suffix[i+1] - suffix[i + ai + 1]) % MOD
        
        # 2. 计算分子: (ai + 1 + sum)
        numerator = (ai + 1 + range_sum) % MOD
        
        # 3. 计算分母的逆元: ai^-1
        inv_ai = pow(ai, MOD - 2, MOD)
        
        # 4. 更新 dp[i]
        dp[i] = (numerator * inv_ai) % MOD
        
        # 5. 更新后缀和供下一次循环使用
        suffix[i] = (suffix[i+1] + dp[i]) % MOD
        
    print(dp[1])

if __name__ == "__main__":
    solve()
