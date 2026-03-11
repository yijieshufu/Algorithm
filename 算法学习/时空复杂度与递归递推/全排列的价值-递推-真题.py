import os
import sys
it =iter(sys.stdin.read().split())
n = int(next(it))
MOD = 998244353
if n < 2:
    print(0)   
f = [0] * (n + 1)
f[1]=1
for i in range(2,n+1):
  if i == 2:  # 先除去2
    f[i]=f[i-1]
  else:
    f[i]=f[i-1]*i % MOD
ans = (n * (n-1) // 2 * f[n] )%MOD
print(ans)
