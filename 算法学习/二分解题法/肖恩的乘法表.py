import os
import sys
data = sys.stdin.read().split()
n,m,k=map(int,data)
# 确保n小
if n>m: n, m = m, n
# 统计第i行有多少个小于x的
def chack(x):
  cnt = 0
  for i in range(1,n+1):
    cnt +=min(m,x//i)
  return cnt
# 二分法
l,r=1,n*m
ans =r 
while l<=r:
  mid = (l+r)//2
  if chack(mid)>=k:
    ans = mid
    r =mid-1
  else:
    l =mid+1
print(ans)
