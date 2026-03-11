import os
import sys
n = 2024041331404202
ans = 2 # 小于10 里面有 1 和 3满足
q = n //200
r = n % 200
ans += q * 4
for x in [24, 175, 199, 200]:
  if 10 <=x<=r:
    ans+=1
print(ans)
