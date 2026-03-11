import os
import sys
# 请在此输入您的代码
res =0
for i  in range(256):
  for j  in range(256):
    for k  in range(256):
      if i!=j or i!=k or j!=k: # 写多余了
        if k>i and k>j:
          res+=1
print(res)
