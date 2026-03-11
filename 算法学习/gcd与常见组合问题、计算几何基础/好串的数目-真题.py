import os
import sys
it = iter(sys.stdin.read().split())
s = next(it)
n = len(s)
f = [0]*(n)
f[n-1]=n-1
# `f[i]` 代表从第 `i` 个字符开始，**最长的一段**符合规则的楼梯在哪里结束
for i in range(n-2,-1,-1):
  curr = int(s[i])
  nxt = int(s[i+1])
  if nxt == curr or nxt == curr + 1:
    f[i]=f[i+1]
  else:
    f[i]=i

ans = 0 
for l in range(n):
  i = f[l] #第一段
  if i< n-1:
    j = f[i+1] # 第二段
    ans+=(j-l+1) #计算长度
  else:
    ans+=(n-l) # 只有一段 直接到n
print(ans)
