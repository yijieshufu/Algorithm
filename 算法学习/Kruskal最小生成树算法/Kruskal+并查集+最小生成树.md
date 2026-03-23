# 点亮须弥
**【材料】 (Materials)**
- **对象**：$n$ 个传送点（节点），编号 $1 \sim n$。
- **通路**：$m$ 条双向路径，每条路有时间花费 $w_i$。
- **关键道具**：一旦传送点被点亮，旅行者可以在已点亮的传送点之间**瞬间传送**。
- **起点**：传送点 1 会自动点亮。
- **规模**：$n \le 10^5$，$m \le 10^6$。这是一个较大的数据规模，必须使用高效算法。  
**【条件】 (Constraints)**
- **瞬间传送**：这意味着如果你在点 $A$（已点亮），要去点 $B$（未点亮），你可以瞬间传送到离 $B$ 最近的任何一个已点亮节点，然后走最短的那条路过去。
- **全点亮要求**：必须点亮所有 $n$ 个点。
- **本质逻辑**：为了让总时间最少，每一步点亮新节点时，我们都要选择连接“已点亮集合”与“未点亮集合”之间权重最小的那条边。  
**【目的】 (Objective)**
- 计算点亮所有传送点所需的**最小总时间**。如果无法全部点亮，输出 $-1$。
## 🧠 逻辑分析：为什么是最小生成树？
1. **初始状态**：只有节点 1 在“已点亮”集合里。
2. **扩张过程**：
    - 我们要从“已点亮”集合里选一个点，走向一个“未点亮”的点。
    - 一旦新点被点亮，它就加入了“瞬间传送阵营”。
    - 为了让总时间最少，我们每次都选花费最小的那条路。
3. **算法选择**：
    - 这完美符合 **Prim 算法**或 **Kruskal 算法**的定义。
    - 鉴于边数 $m$ 达到 $10^6$，且节点数 $n$ 为 $10^5$，**Kruskal 算法**配合并查集（DSU）在 Python 中通常更易于编写且逻辑清晰。

使用了 Kruskal算法 来求解最小生成树  
	先按照权重排序  
	并查集  
		find路径压缩  
		合并的时候 累计权重  
		直到到达n-1条边
## 代码

```python
import sys
import heapq
it = iter(sys.stdin.read().split())
n,m= int(next(it)),int(next(it))
a = []
for _ in range(m):
  u,v,w= int(next(it)),int(next(it)),int(next(it))
  a.append((w,u,v))
a.sort() # 按照权重排序
f = list(range(n+1)) # 父亲数组
def find(x):
  if x!=f[x]:
    f[x] = find(f[x])
  return f[x]
ans = 0 # 最小生成树总全值
count = 0 # 连接的边数
for w,u,v in a:
  root_u,root_v = find(u),find(v)
  if root_u != root_v: # 不是一个环（集合） 加入进来
	f[root_u] = root_v
    ans+=w
    count+=1
    if count == n-1:break
if n == 1:
  print(0)
elif count == n-1:
  print(ans)
else:
  print(-1)
```
