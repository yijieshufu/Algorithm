import os
import sys
# 请在此输入您的代码
res = 1
num=1
while res < 23:
  if bin(num).count('1')==3:
    res+=1
  num+=1
print(num)
