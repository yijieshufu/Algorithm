# 黄金树
**【材料】 (Materials)**
- **基础数据**：一棵拥有 $n$ 个节点的二叉树，编号为 $1 \sim n$。
- **节点属性**：每个节点 $i$ 都有一个权重 $w_i$。
- **结构信息**：给出每个节点的左儿子 $l_i$ 和右儿子 $r_i$（$-1$ 表示不存在）。
- **起始点**：$1$ 号点固定为根节点。  
**【条件】 (Constraints)**
- **黄金指数 (GI) 定义**：
    1. **根节点**：$GI_{root} = 0$。
    2. **向左走**：左儿子的 $GI = 父节点 GI + 1$。
    3. **向右走**：右儿子的 $GI = 父节点 GI - 1$。  
**【目的】 (Objective)**
- 遍历整棵树，找出所有黄金指数为 $0$ 的节点。
- 计算这些节点的**权重之和**并输出。
## 分析
本质上 就是 标记位（黄金指数为0）的权重
## 代码
```python
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
w = [0]+[int(next(it)) for _ in range(n)]
a = [(0,0)]
for _ in range(n):
  l = int(next(it))
  r = int(next(it))
  a.append((l,r)) # 读入左右子节点
ans = 0
def DFS(u,gi):
  global ans
  if u == -1: return # 表示不存在
  if gi ==0:ans+=w[u]
  l,r = a[u]
  DFS(l,gi+1)
  DFS(r,gi-1)
DFS(1,0)
print(ans)
```