import os
import sys
# 请在此输入您的代码
hp =2025
res = 1
while hp>=0:
  damage =0
  damage +=5
  if res % 2==1:
    damage+=15
  else:
    damage+=2
  if res % 3==1:
    damage+=2
  elif res % 3==2:
    damage+=10
  elif res % 3==0:
    damage+=7
  hp-=damage
  if hp <= 0:
    break
  res+=1
print(res)
