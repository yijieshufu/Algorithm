import os
import sys
it = iter(sys.stdin.read().split())
N = int(next(it))
M = int(next(it))
cnt =0
def hanoi(n,a,b,c):
  global cnt
  if n==1: # 只有一个圆盘的时候
    cnt+=1
    if cnt == M:
      print(f"#{n}: {a}->{c}")
    return
  hanoi(n-1,a,c,b) # 第一步：把上面n-1看成整体 从 a-c-b
  cnt+=1  # 移动底部的圆盘 此时A剩下最大的圆盘 第cnt次移动
  if cnt==M:
    print(f"#{n}: {a}->{c}")
  hanoi(n-1,b,a,c) # 再把移动到b的 n-1个圆盘移动到通过a移动到c
hanoi(N,"A","B","C")
