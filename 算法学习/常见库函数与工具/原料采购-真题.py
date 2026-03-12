import os
import sys
import heapq
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
o = int(next(it))
ans = float('inf')
h = []
cnt = 0 # 容量
sum_p= 0 # 费用
for _ in range(n):
  a = int(next(it)) # 价格
  b = int(next(it)) # 库存
  c = int(next(it)) # 距离
  if cnt < m : # 直接拿到车里面
    take = min(b,m-cnt) 
    sum_p += take*a
    cnt +=take
    heapq.heappush(h,[-a,take])
    b-=take  
  if b > 0 and h and a < -h[0][0]: # 判断当前是否可换
    replace = 0
    while b > 0 and h and a < -h[0][0]: # 一直换
      a_val,b_cnt = heapq.heappop(h) #拿出堆顶的 来换
      can_replace = min(b_cnt,b) # 能换多少
      sum_p += (a+a_val)*can_replace #计算差值
      b_cnt-=can_replace;b-=can_replace
      replace+=can_replace
      if b_cnt>0:
        heapq.heappush(h,[a_val,b_cnt])
        break
    if replace>0:
      heapq.heappush(h,[-a,replace])
  if cnt==m:
    ans =min(ans,sum_p+c*o)
print(ans if ans != float('inf') else -1)
