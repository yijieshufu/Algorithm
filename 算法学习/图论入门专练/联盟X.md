
# 题目描述
给定 $n$ 个点和 $m$ 条边，求图中所有连通分量中，**节点数最少**的分量所包含的节点数量。
- **数据范围**：$n, m \le 2 \times 10^4$。
- **时限**：Python 3s，非常充裕。
# 分析
**并查集 (DSU) + 动态大小维护**。
- **原因**：题目涉及点的合并（修建道路）以及查询连通性（村子联盟）。
- **核心需求**：不仅要判断两个点是否连通，还要实时记录每个集合（联盟）内部的成员总数。

- **初始化**：定义父节点数组 `p`，初始时 `p[i] = i`；定义大小数组 `sz`，初始时 `sz[i] = 1`。
- **路径压缩**：编写 `find` 函数，在查找根节点的同时压缩路径，保证后续操作接近 $O(1)$。
- **合并逻辑**：读取边 $(u, v)$，若两点不在同一集合，则合并它们，并将其中一个根节点的大小累加到另一个根节点上。
- **结果计算**：遍历 $1 \sim n$，对于所有满足 `p[i] == i` 的根节点，取其 `sz[i]` 的最小值。
# 笔记

## 代码

```python
import sys 
sys.setrecursionlimit(10000)
# 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it));m = int(next(it))

# 初始化 父列表 和sz
p = list(range(n+1))
sz = [1]*(n+1) #节点数量

# find(路径压缩)
def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]
# 合并边
for _ in range(m):
    u = int(next(it));v = int(next(it))
    u_root = find(u);v_root = find(v)
    if u_root!=v_root:
        p[u_root]=v_root
        sz[v_root]+=sz[u_root]
# 统计 各个联通的数量 取最小值
ans = n+1
for i in range(1,n+1):
    if p[i]==i:
        ans = min(ans,sz[i])
print(ans)
```
