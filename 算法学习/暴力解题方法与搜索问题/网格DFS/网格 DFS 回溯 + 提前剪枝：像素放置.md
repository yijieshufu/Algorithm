# 像素放置
在 $n \times m$ 网格中填入 0 或 1。  
带数字的格子要求其周围 $3 \times 3$ 范围内 1 的总数必须**等于该数字**。  
求合法的全盘填充方案。
# 分析 

预设 b f  
	得到i,j为中心的 然后累计和

# 代码
```python
import sys 
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
g = [next(it) for _ in range(n)]
ans = [[0]*m for _ in range(n)]
def dfs(a):
  if a == n*m:
    for b in ans :
      print("".join(map(str,b)))
    return True
  b,f = divmod(a,m)
  for v in (0,1):
    ans[b][f] = v # 走到这个位置了 b f
    ok = True
	
    for i in range(n):
      for j in range(m):
        if g[i][j] != '_' and min(n-1,i+1) == b and min(m-1,j+1) == f: # 刚好影响到了 b f 
          s = 0
          # 以 i,j 为中心的 0 1 的和
          for x in range(max(0,i-1),min(n,i+2)):
            for y in range(max(0,j-1),min(m,j+2)):
              s+=ans[x][y]
			  
          if s != int(g[i][j]):
            ok = False
      if not ok:
        break
    if ok and dfs(a+1):
      return True
  return False
dfs(0)
```
