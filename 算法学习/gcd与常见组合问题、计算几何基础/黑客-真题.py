import os
import sys
from collections import Counter
it = iter(sys.stdin.read().split())
mod =1000000007
# 1. 预处理阶乘与逆元
def prepare(limit):
  fac = [1]*(limit+1)
  inv = [1]*(limit+1)
  for i in range(1,limit+1):
    fac[i] = fac[i-1]*i % mod
  inv[limit] = pow(fac[limit],mod-2,mod)
  for i in range(limit-1,-1,-1):
    inv[i] = inv[i+1]*(i+1)%mod
  return fac,inv
K = int(next(it))
nums=[int(next(it)) for _ in range(K)]
counts= Counter(nums)
X = K - 2
fac,inv = prepare(K)
denom_inv = 1
for val in counts:
  denom_inv = denom_inv * inv[counts[val]] %mod
W = (fac[X]* denom_inv)% mod
total_contribution = 0
d = 1
while d * d <= X:
  if X % d == 0:
    y = X // d 
    if d == y :
      if counts[d]>=2:
        term = (counts[d]*(counts[d]-1))%mod
        total_contribution = (total_contribution +term) % mod
    else:
      if counts[d]>=1 and counts[y]>=1:
        term = (2*counts[d]*counts[y])%mod
        total_contribution = (total_contribution +term) % mod
  d+=1
print((W*total_contribution)%mod)
