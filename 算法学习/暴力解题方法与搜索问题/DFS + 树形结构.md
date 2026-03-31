# 团建-真题
- **背景**：小蓝和朋友各有两棵树（大小分别为 $n$ 和 $m$），每个节点都有一个正整数权值。
- **规则**：两人同时从各自树的**根节点（1 号节点）** 出发，向下走到某个叶子节点。路径上经过的**权值**构成一个**序列。**
- **得分**：两人路径序列的**最长公共前缀**（Longest Common Prefix, LCP）的长度。
- **特殊条件**：对于树中任意一个节点，其所有**子节点的权值互不相同**。
- **目标**：计算两人最多能得到多少分。
# 分析
#### ① 问题的转化
由于必须从根节点出发，且求的是“最长公共前缀”，这意味着如果根节点的权值都不一样，得分直接为 0。如果一样，则得分为 1，并继续看它们的子节点中是否有权值相同的。
#### ② 关键约束：子节点权值互不相同
这是本题最重要的“减负”条件。
- 如果节点 $A$（在树 1）和节点 $B$（在树 2）的权值相同，我们要看它们的儿子。
- 因为每个节点的儿子权值都不一样，所以对于一个权值 $W$，在 $A$ 的儿子里最多只有一个，在 $B$ 的儿子里也最多只有一个。
- **这意味着：匹配关系是唯一的！** 我们不需要像求“最长公共子序列”那样去写复杂的动态规划，只需要顺着权值相同的节点一直往下走即可。
#### ③ 算法设计
1. **建树**：将给定的无向边转化为有向的父子关系。
2. **字典优化**：为了快速找到“权值为 $W$ 的儿子是谁”，我们为每个节点建立一个字典（Map），存储 `{儿子权值: 儿子编号}`。
3. **DFS 遍历**：从 `(root1, root2)` 开始递归。如果当前两个节点匹配，尝试在它们的子节点中寻找权值相同的配对。
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
# 建立邻接表
def build_t(n,w):
  g=[[] for _ in range(n+1)]
  for _ in range(n-1):
    u=int(next(it));v=int(next(it))
    g[u].append(v);g[v].append(u)
  
  t = [ {} for _ in range(n+1)]
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
```
