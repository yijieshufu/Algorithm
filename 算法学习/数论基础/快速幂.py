import os
import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
b = int(next(it))
p = int(next(it))
k = int(next(it))
def quick_pow(b,p,k):
  res = 1
  while p > 0: 
    if p & 1:
      res = res * b % k
    b = b * b % k
    p >>= 1
  return res
print(quick_pow(b,p,k))
