import os
import sys
res=0
# 请在此输入您的代码
for i in range(1,2026):
  if i*i*i %10==3:
    res+=1
print(res)
