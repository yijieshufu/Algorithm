import os
import sys
it =iter(sys.stdin.read().split())

def solve():
  m = int(next(it))
  n = int(next(it))
  g=[['0']*(n+2) for _ in range(m+2)]
  for i in range(1,m+1):
    row = next(it) #一次读入一行
    for j in range(1, n + 1):
      g[i][j] = row[j-1] #下标为0开始
  vis=[[False]*(n+2) for _ in range(m+2)] # 标记位
  ans = 0
  q = [(0,0)] # q列表用来存海水弥漫的地方
  vis[0][0]=True
  while q:
    r,c=q.pop(0)
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]: # 八个方位
      nr=r+dr;nc=c+dc
      if 0<=nr<m+2 and 0<=nc<n+2 and not vis[nr][nc]:#BFS
        if g[nr][nc] =='0':
          vis[nr][nc]=True
          q.append((nr,nc))
        else:
          ans+=1
          lan_q =[(nr,nc)]
          vis[nr][nc]=True
          while lan_q: #BFS
            lr,lc=lan_q.pop(0)
            for ldr,ldc in[(-1,0),(1,0),(0,-1),(0,1)]:
              nlr=lr+ldr;nlc=lc+ldc
              if 0<=nlr<m+2 and 0<=nlc<n+2 and not vis[nlr][nlc] and g[nlr][nlc] =='1':
                vis[nlr][nlc]=True
                lan_q.append((nlr,nlc))
  print(ans)
t = int(next(it))
for _ in range(t):
  solve()
