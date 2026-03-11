import sys
from bisect import bisect_left,bisect_right
# 输入数据
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
# 重新排序
s=sorted(a)
# 计算 中位数的分布
mid_val = s[n//2]
cntl = bisect_left(s,mid_val)
cntr = n-bisect_right(s,mid_val)
# 确定中位数
if cntl > cntr:
  target = mid_val
else:
  target = mid_val+1
ans =[]
for x in a :
  l = bisect_left(s,x)
  r = n-bisect_right(s,x)
  if r <= l:
    ans.append(0)
  else:
    ans.append(max(0,target-x))
print(*ans)
