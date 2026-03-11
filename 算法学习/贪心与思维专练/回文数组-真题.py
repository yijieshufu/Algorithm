import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(x) for x in it]
diffs = [a[i] - a[n-1-i] for i in range(n // 2)]
ans = 0
prev = 0
for x in diffs:
  if x * prev > 0:  # 方向相同，尝试搭顺风车
    # 只有当前坑更深，才需要额外付钱
    ans += max(0, abs(x) - abs(prev))
  else:             # 方向不同，之前的操作帮不上忙
    ans += abs(x)
  prev = x
print(ans)
