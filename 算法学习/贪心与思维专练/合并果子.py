import os
import sys
import heapq 
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(x) for x in it]
heapq.heapify(a) # 堆化
res = 0 
while len(a)>1:
  s = heapq.heappop(a) + heapq.heappop(a)
  res +=s
  heapq.heappush(a,s)
print(res)
