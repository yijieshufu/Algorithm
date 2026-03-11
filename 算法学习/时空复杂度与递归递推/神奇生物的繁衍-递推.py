import os
import sys

# 请在此输入您的代码
it =iter(sys.stdin.read().split())
n=int(next(it))
mod = 10**9+7
dp = [0]*(n+2)
for i in range(1,n+2):
  if i <= 5:
    dp[i]=1
  else:
    dp[i]=(dp[i-1]+dp[i-5])%mod
print(dp[n+1])
