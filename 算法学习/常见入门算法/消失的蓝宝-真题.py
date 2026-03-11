import os
import sys
# 请在此输入您的代码
A = 20250412
B = 20240413
def gcd(x,y):
  while y:
    x,y=y,x % y
  return x
gcd = gcd(A,B)
lcm= A*B // gcd
print(lcm-A-B)
