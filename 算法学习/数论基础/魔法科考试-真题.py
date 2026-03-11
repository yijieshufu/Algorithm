import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a=[]
b=[]
for _ in range(n):
  a.append(int(next(it)))
for _ in range(m):
  b.append(int(next(it)))
a_set=set(a)
b_set=set(b)
limit = 40000
is_prime = [True] * (limit + 1)
is_prime[0]=is_prime[1] = False # 1 不是质数
for i in range(2,int(limit**0.5) + 1):
  if is_prime[i]:
    for j in range (i*i,limit+1,i):
      is_prime[j]=False
bits_b = 0
for x in b_set:
  bits_b |=(1 << x)
sum = 0
for x in a_set:
  sum |=(bits_b << x )
res = 0
for p in range(2,m+n+1):
  if is_prime[p]:
    if (sum>>p&1):
      res+=1
print(res)
