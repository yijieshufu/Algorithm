import os
import sys
# 请在此输入您的代码
it=iter(sys.stdin.read().split())
N = int(next(it))
MOD = 10**9+7
dp=[0]* (N+1)
ans = 0
for i in range(1,N):
  dp[i]=(i*(N-i)*(N-i)) % MOD
  ans  = (ans+dp[i])% MOD
print(ans)
