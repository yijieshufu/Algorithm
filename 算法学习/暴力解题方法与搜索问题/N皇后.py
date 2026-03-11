import sys
it = iter(sys.stdin.read().split())
N = int(next(it))
col = [False]*30
gd = [False]*30
udg = [False]*30
ans = 0
def dfs(u):
  global ans
  if u == N:
    ans+=1
    return
  for i in range(N): 
    if not col[i] and not gd[u+i] and not udg[u-i+N]: # 正对角线 u+i 和 反对角线u-i+n是定值
      col[i]=gd[u+i]=udg[u-i+N]=True
      dfs(u+1)
      col[i]=gd[u+i]=udg[u-i+N]=False
dfs(0)
print(ans)
