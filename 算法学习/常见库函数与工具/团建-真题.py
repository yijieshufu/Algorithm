import os
import sys

sys.setrecursionlimit(1000000)

it = iter(sys.stdin.read().split())
n=int(next(it))
m=int(next(it))
# 权值
w1 =[0]+[int(next(it)) for _ in range(n)]
w2 =[0]+[int(next(it)) for _ in range(m)]
# 建立邻接表
def build_t(n,w):
  g=[[] for _ in range(n+1)]
  for _ in range(n-1):
    u=int(next(it));v=int(next(it))
    g[u].append(v);g[v].append(u)
  
  t = [{}for _ in range(n+1)]
  def pre(u,p):
    for v in g[u]:
      if v!=p:
        t[u][w[v]]=v # 列表为u的节点里面出入了 key:权重 val:儿子节点编号
        pre(v,u)
  pre(1,-1)
  return t
t1 = build_t(n,w1)
t2 = build_t(m,w2)
def dfs(u,v):
  mx=0
  for val,nxt_u in t1[u].items():
    if val in t2[v]:
      nxt_v =t2[v][val]
      res = dfs(nxt_u,nxt_v)
      if res>mx:mx=res
  return 1+mx
if w1[1]!=w2[1]:
  print(0)
else:
  print(dfs(1,1))
