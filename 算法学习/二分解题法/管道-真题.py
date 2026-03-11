import os
import sys

# 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it)) 
a = [(int(next(it)),int(next(it))) for _ in range(n)]
# check 函数
def check(t):
  # 计算区间
  q =[]
  for i in range(n):
    l,s=a[i]
    if t>=s:
      d = t-s
      q.append((max(1,l-d),min(m,l+d)))
  if not q:return False
  q.sort()
  if q[0][0]>1:return False
  curr = q[0][1]
  # 裁剪区间
  for i in range(len(q)):
    if q[i][0]<curr+1:
      curr = max(curr,q[i][1])
    else:
      break
  return curr>=m
# 二分法
l, r, ans = 0, 2000000000, 0
while l<=r:
  mid = (l+r)//2
  if check(mid):
    ans = mid
    r = mid-1
  else:
    l = mid+1
print(ans)
