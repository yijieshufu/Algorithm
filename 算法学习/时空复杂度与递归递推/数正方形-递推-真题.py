import os
import sys
# 请在此输入您的代码
it=iter(sys.stdin.read().split())
N = int(next(it))
MOD = 10**9+7
dp=[0]* (N+1)
ans = 0
for i in range(1,N): # i代表边长为i的正方形
  dp[i]=(i*(N-i)*(N-i)) % MOD # 边长为i的正方形里面可以画i个正方形 N-i代表每条边可以取的位置  x y一样则乘
  ans  = (ans+dp[i])% MOD
print(ans)
