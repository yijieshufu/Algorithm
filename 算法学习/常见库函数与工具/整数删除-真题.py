import os
import sys
import heapq
it = iter(sys.stdin.read().split())
n = int(next(it))
k = int(next(it))
V =[int(next(it)) for _ in range(n)]
L = [i - 1 for i in range(n)] # L[i] 存 i 的左邻居，0 的左邻居是 -1
R = [i + 1 for i in range(n)] # R[i] 存 i 的右邻居
R[n - 1] = -1
hq = []
for i in range(n):
  heapq.heappush(hq, (V[i], i))
deleted = [False] * n 
ops = 0
while ops<k and hq:
  val, idx = heapq.heappop(hq)
  if deleted[idx] or val!=V[idx]: # 废纸不看 
    continue
  deleted[idx]=True
  ops+=1
  left_idx = L[idx]
  right_idx = R[idx]
  if left_idx != -1:
    V[left_idx] += val #值分给左边
    R[left_idx] = right_idx # 更新右邻居
    heapq.heappush(hq,(V[left_idx],left_idx)) #将分了钱的新左邻居添加进去 加入新纸
  if right_idx != -1: # 同理
    V[right_idx] += val
    L[right_idx] = left_idx
    heapq.heappush(hq,(V[right_idx],right_idx))
ans = (str(V[i]) for i in range(n) if not deleted[i])
sys.stdout.write(" ".join(ans)+"\n")
