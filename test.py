import sys
from bisect import bisect_left, bisect_right

it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]

# 排序用于二分统计
s = sorted(a)

# 计算全局中位数的左右分布
mid_val = s[n // 2]
cntL = bisect_left(s, mid_val) # 小于中位数
cntR = n - bisect_right(s, mid_val) # 大于中位数

# 核心策略：确定对于需要补题的学生，目标分数 T 是多少
if cntL > cntR:
    target = mid_val
else:
    target = mid_val + 1

ans = []
for x in a:
    # 统计当前学生比他多/少的人数
    curL = bisect_left(s, x)
    curR = n - bisect_right(s, x)

    if curR <= curL:
        ans.append(0)
    else:
        # 不达标，则补齐到 target
        ans.append(max(0, target - x))

print(*(ans))