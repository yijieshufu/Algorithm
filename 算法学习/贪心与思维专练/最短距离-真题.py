import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
x = [int(next(it)) for _ in range(n)]
y = [int(next(it)) for _ in range(n)]
x.sort()
y.sort()
ans = 0
for i in range(n):
  # abs() 计算一维直线距离
  ans += abs(x[i] - y[i])
print(ans)
