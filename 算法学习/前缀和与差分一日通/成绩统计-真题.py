import os
import sys

it = iter(sys.stdin.read().split())
n = int(next(it))
k = int(next(it))
t = int(next(it))
a = [int(next(it)) for _ in range(n)]

def check(x):
  sub = sorted(a[:x]) # 只排序前x个
  curr_sum = 0;curr_sq_sum=0
  for i in range(k):
    curr_sum +=sub[i] # 和
    curr_sq_sum +=sub[i]*sub[i] # 平方
  target = t*k*k
  if k * curr_sq_sum - curr_sum * curr_sum < target: # 方差公式
    return True
  for i in range(x-k): # 区间移动
    left_val = sub[i] #左边的值
    right_val = sub[i + k] #右边的值
    curr_sum += right_val - left_val # 计算当前的区间
    curr_sq_sum+= right_val*right_val-left_val*left_val
    # 实时检查当前窗口是否达标
    if k * curr_sq_sum - curr_sum * curr_sum < target:
        return True
  return False

# 二分法
ans = -1
low = k 
high = n 
while low<=high:
  mid = (low+high)//2
  if check(mid):
    ans = mid # 要检查的人数
    high=mid-1
  else:
    low=mid+1
print(ans)
