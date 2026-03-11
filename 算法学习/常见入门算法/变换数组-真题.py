import os
import sys
# 请在此输入您的代码
it =iter(sys.stdin.read().split())
n=int(next(it))
b=[0]+[int(next(it)) for i in range(n)]
m=int(next(it))
for _ in range(m):
  for k in range(1,n+1):
    b[k]=b[k]*bin(b[k]).count('1')
print(*(b[i] for i in range(1, n + 1)))
