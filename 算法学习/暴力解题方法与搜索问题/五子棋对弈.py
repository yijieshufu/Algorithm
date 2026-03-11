import os
import sys
import itertools

# 1. 预处理 获胜线
lines =[] # 胜利集合
#行
for i in range(0,25,5):
  lines.append((set(range(i,i+5))))
#列
for j in range(5):
  lines.append((set(range(j,25,5))))  # 存入的集合
#对角线
lines.append({0,6,12,18,24})
lines.append({4,8,12,16,20})
all_pos = set(range(25))
ans = 0 
# 2. 白棋 combinations
for write in itertools.combinations(range(25),13):
  w_set=set(write) # 白色集合
  b_set=all_pos-w_set # 剩下的是黑色集合
  is_draw = True # 预定平局
  for line in lines:
    if line<= w_set or line<= b_set: # 黑或者白 有个是胜利 集合
      is_draw =False
      break
  if is_draw:ans+=1 
print(ans)
