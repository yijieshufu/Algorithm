# [岛屿个数](https://www.lanqiao.cn/courses/52517/learning/?id=5027778&compatibility=false)
**核心动作**：
- **网格组成**：$M \times N$ 的网格，'0' 代表海水，'1' 代表陆地。
- **连通规则**：陆地仅在**上下左右**（4方向）相邻时连为同一岛屿。
- **子岛屿定义**：如果岛屿 B 被岛屿 A 形成的“环”完全包围，则 B 是 A 的子岛屿。
- **任务**：统计**非子岛屿**的数量。  
即：如果一个岛屿在另一个岛屿的“肚子”里，就不计入总数。
# 分析
- **本质**：非子岛屿 = **能接触到外海的岛屿**。
- **海水 8 方向**：因为海水可以从陆地的对角线缝隙钻过去。
- **陆地 4 方向**：标准的岛屿连通判定。
- **动作**：
    1. 从外海（补一圈 '0'）开始跑 BFS。
    2. 如果遇到 **海水**：按 **8 方向** 扩散。
    3. 如果遇到 **陆地且未访问过**：这是一个新岛屿（`ans += 1`），立刻启动一个内部 BFS 按 **4 方向** 把这个岛屿全部标记掉（消减岛屿）。
# 代码
```python
import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
for _ in range(t):
  m,n= int(next(it)),int(next(it))
  g = [['0']*(n+2) for _ in range(m+2)] # 二维 扩展2行2列 为0
  # 读入地图
  for i in range(1,m+1):
    row = next(it) # 下标从 0 开始
    for j in range(1,n+1):
      g[i][j] = row[j-1]
  vis = [[False]*(n+2) for _ in range(m+2)] # 直接由地图 创建访问数组
  ans = 0
  q = [(0,0)] # 从(0,0) 开始
  vis[0][0] = True
  while q:
    r , c = q.pop(0)
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]: # 8个方向
      nr = dr+r;nc = dc+c
      if 0<=nr<m+2 and 0<=nc<n+2 and not vis[nr][nc]:
        if g[nr][nc] == '0': # 海水
          vis[nr][nc] = True
          q.append((nr,nc)) 
        else: # 遇到陆地了
          ans +=1 # 相当于找到了一个岛屿了
          lan_q = [(nr,nc)] # 陆地起点遍历
          vis[nr][nc] = True
          while lan_q:
            lr ,lc = lan_q.pop(0)
            for ldr,ldc in [(-1,0),(1,0),(0,-1),(0,1)]:
              nlr = ldr+lr;nlc = ldc+lc
              if 0<=nlr<m+2 and 0<=nlc<n+2 and not vis[nlr][nlc]:
                if g[nlr][nlc] == '1': # 陆地
                  vis[nlr][nlc] = True
                  lan_q.append((nlr,nlc)) 
  print(ans)
```
