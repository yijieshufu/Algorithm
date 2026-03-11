import os
import sys
it = iter(sys.stdin.read().split())
N = int(next(it))
M = int(next(it))
a = [0]+[int(next(it)) for _ in range(N)]
sum = [0]*(N+1) 
for i in range(1,N+1):
  sum[i]=sum[i-1]+a[i] # 计算区间的前缀和
for _ in range(M):
  L=int(next(it))
  R=int(next(it))
  print(sum[R]-sum[L-1])
