import os
import sys
from collections import deque

# 请在此输入您的代码
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
g = [[int(next(it)) for _ in range(m)] for _ in range(n)]
x1= int(next(it))-1;y1= int(next(it))-1;x2= int(next(it))-1;y2= int(next(it))-1
dist = [[-1] * m for _ in range(n)]
queue = deque([(x1,y1)])
dist[x1][y1]=0
found= False
dx =[-1,1,0,0]
dy =[0,0,1,-1]
while queue:
  cur_x,cur_y=queue.popleft()
  if cur_x==x2 and cur_y==y2:
    found=True
    print(dist[cur_x][cur_y])
    break
  for i in range(4):
    nx=cur_x+dx[i];ny=cur_y+dy[i]
    if 0<=nx<=n-1 and 0<=ny<=m-1:
      if g[nx][ny]==1 and dist[nx][ny]==-1 :
        dist[nx][ny]= dist[cur_x][cur_y]+1
        queue.append((nx,ny))
if not found:
  print(-1)
