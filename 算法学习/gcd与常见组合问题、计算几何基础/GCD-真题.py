import os
import sys
it=iter(sys.stdin.read().split())
a = int(next(it))
b = int(next(it))
if a > b: # b最大
  a,b=b,a
diff = b - a
rem = a % diff #  计算 a 距离上一个 D 的倍数多出了多少 (余数)
if rem == 0:
  print(diff)
else:
  print(diff-rem)
