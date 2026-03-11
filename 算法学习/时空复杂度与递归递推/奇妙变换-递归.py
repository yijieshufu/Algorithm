import os
import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
n = int(next(it))
mod = 998244353
f = [0]* (n+1)
for i in range (1,n+1):
  if i <=10:
    f[i] = i * (i-1) % mod 
  else:
    f[i]=2*i*f[i-6] % mod
print(f[n])
