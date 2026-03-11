import os
import sys
# 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it))
k = int(next(it))
a = [int(next(it)) for _ in range(n)]
# 二分判断函数
def check(mid):
  # 计算前缀和：定义前缀和列表
  s = [0]*(n+1)
  for i in range(n):
    val = 1 if a[i]>=mid else -1
    s[i+1] = s[i]+val
  # 长度不小于k的连续子系列
  min_pre = 0
  for j in range(k,n+1):
    if s[j-k]< min_pre:
      min_pre=s[j-k]
    if s[j]-min_pre>=1:
      return True
  return False
# 二分模板
l,r =1,max(a)
ans =1 
while l<=r:
  mid = (l+r)//2
  if check(mid):
    ans = mid
    l = mid+1
  else:
    r = mid-1
print(ans)
