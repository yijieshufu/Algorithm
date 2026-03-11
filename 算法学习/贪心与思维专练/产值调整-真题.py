import os
import sys
it = iter(sys.stdin.read().split())
t = int(next(it))
for _ in range(t):
  a,b,c,k=int(next(it)),int(next(it)),int(next(it)),int(next(it))
  limit = k
  if k>100:
    limit=100 + k%2
  for i in range(limit):
    na = (b+c)//2
    nb = (a+c)//2
    nc = (a+b)//2
    if na==a and nb ==b and nc ==c:
      break
    a,b,c=na,nb,nc
  print(a,end=" ");print(b,end=" ");print(c)
