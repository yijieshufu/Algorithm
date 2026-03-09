import os
import sys
limit = 2000000
N = 100002
is_prime = [True] * (limit + 1)
is_prime[1] = False # 1 不是质数
primes = []
for i in range(2,limit+1):
  if is_prime:
    primes.append(i)
    # 如果已经找到了足够数量的质数，就可以停下了
    if len(primes) == N:
        print(primes[-1])
        break
    for j in range (i*i,limit+1,i):
      is_prime[j]=False
