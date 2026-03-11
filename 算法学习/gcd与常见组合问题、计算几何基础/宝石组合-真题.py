import os
import sys

# 请在此输入您的代码
it = iter(sys.stdin.read().split())
max_h=0
limit=10**5+1
cnt = [0]*(limit)
n =int(next(it))

for _ in range(n):
  h = int(next(it))
  cnt[h]+=1 # 记录亮度有多少颗
  if h>max_h:
    max_h=h # max_h 亮度最高的宝石

for g in range(max_h,0,-1): #最大公约数不能超过本身，那么从最大的数开始速度更快
  res=[]
  for m_g in range(g,max_h+1,g): # 只看g的倍数
    if(cnt[m_g])>0:
      take=min(cnt[m_g],3-len(res)) # 完美处理了 现在还差几颗
      for _ in range(take):
        res.append(m_g)
      if len(res)==3:
	        print(*res)
        sys.exit()
