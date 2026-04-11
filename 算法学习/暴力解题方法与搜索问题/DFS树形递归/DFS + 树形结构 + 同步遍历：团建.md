# 团建-真题
- **背景**：小蓝和朋友各有两棵树（大小分别为 $n$ 和 $m$），每个节点都有一个正整数权值。
- **规则**：两人同时从各自树的**根节点（1 号节点）** 出发，向下走到某个叶子节点。路径上经过的**权值**构成一个**序列。**
- **得分**：两人路径序列的**最长公共前缀**（Longest Common Prefix, LCP）的长度。
- **特殊条件**：对于树中任意一个节点，其所有**子节点的权值互不相同**。
- **目标**：计算两人最多能得到多少分。
# 分析
## 代码
```python
import os
import sys

sys.setrecursionlimit(1000000)
it = iter(sys.stdin.read().split())
n=int(next(it))
m=int(next(it))
# 权值
w1 =[0]+[int(next(it)) for _ in range(n)]
w2 =[0]+[int(next(it)) for _ in range(m)]

def build_t(n,w):
  g = [[] for _ in range(n+1)]
  # 添加边的关系
  for _ in range (n-1):
    u,v = int(next(it)),int(next(it))
    g[u].append(v);g[v].append(u)
  # 字典树
  t = [{} for _ in range(n+1)] # u节点下 权值的儿子节点
  def pre(u,p):
    for v in g[u]:
      if v!= p: 
        t[u][w[v]] = v
        pre(v,u)
  pre(1,-1)
  
  return t 

t1 = build_t(n,w1)
t2 = build_t(m,w2)

# 同步遍历
def dfs(u,v):# u 和 v 两棵树
  mx = 0 
  for val,nxt_u in t1[u].items(): # 当前 u 中的权重 和 儿子节点
    if val in t2[v]: # 判断v树中是否有一样的权值
      nxt_v = t2[v][val] # 有的话 找到儿子节点
      res = dfs(nxt_u,nxt_v) # 一起往下走
      if res > mx :mx = res # 记录 最大深度
  return 1+mx
if w1[1]!= w2[1]:
  print(0)
else:
  print(dfs(1,1))
```
