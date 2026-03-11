import os
import sys
n = 28
k = 14
fac = [1]*(n+1)
for i in range(1,n+1): #阶乘
  fac[i]=i*fac[i-1]
comb = fac[n] // (fac[n-k] * fac[k])
d = [0]*(k+1)
if k>=1:d[1]=0
if k>=2:d[2]=1
for i in range(3,k+1):
  d[i] = (i-1)*(d[i-1]+d[i-2])
print(comb*d[k])
