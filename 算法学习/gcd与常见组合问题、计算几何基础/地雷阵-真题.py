import os
import sys
import math

it = iter(sys.stdin.read().split())

n = int(next(it))
intervals = []

Limit_L=0;Limit_R=math.pi/2

for _ in range(n):
  x = int(next(it))
  y = int(next(it))
  r = int(next(it))

  dist = math.sqrt(x**2+y**2)
  mid_angle = math.atan2(y,x)
  delta = math.asin(r/dist)
  
  L=max(Limit_L,mid_angle-delta)
  R=min(Limit_R,mid_angle+delta)

  if L<R:
    intervals.append((L,R))

if not intervals:
        print(f"{1.000:.3f}")

intervals.sort()

merged_len = 0.0

cur_start, cur_end = intervals[0]

for i in range(1,len(intervals)):
  nxt_start, nxt_end = intervals[i]
  if nxt_start<=cur_end:
    cur_end = max(cur_end,nxt_end)
  else:
    merged_len +=(cur_end-cur_start)
    cur_start, cur_end = nxt_start, nxt_end


merged_len +=(cur_end-cur_start)
total_range = Limit_R - Limit_L
safe_prob = (total_range - merged_len) / total_range

# 保证结果不小于 0 (防止浮点误差)
print(f"{max(0.0, safe_prob):.3f}")
