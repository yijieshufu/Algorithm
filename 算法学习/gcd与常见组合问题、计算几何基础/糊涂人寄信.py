import os
import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
for val in it:
  n = int(val)
  d = [0] * 21
  d[1]=0;d[2]=1
  for i in range(3,n+1):
    d[i]=(i-1)*(d[i-1]+d[i-2])
  print(d[n])
