# 815. 公交路线 
给你公交线路 `routes`（每个元素是一条**环行线路**）。 

求从 `source` 到 `target` 所需乘坐的**最少公交车数量**。无法到达返回 `-1`。

# 分析
字典预处理  
	得到每个站点有那些路线

两个维度  
	搜索过的路线  
	搜索过的站点

站点 作为 列表 （站点，换成的次数）

# 代码

```python
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        s = source ; t = target
        if s == t: return 0 # 起点 等于 终点
        # 预处理 相同站 有那几条线
        g = {}
        for i ,route in enumerate(routes):
            for stop in route:
                if stop not in g : g[stop] = []
                g[stop].append(i)
        f = [0] * len(routes) # 已经搜索的路线
        b = {s} # 已经搜索的站点
        q = [(s,0)] # 放入起点,换成次数
        h = 0
        while h <len(q):
            u,ans = q[h]
            h+=1
            if u not in g :continue # 防止 起点不在这所有的站点上
            for i in g[u]: # 找到站点的路线
                if f[i] :continue # 搜索过就跳过
                f[i] = 1 # 标记
                for v in routes[i]:
                    if v == t : return ans+1 # 找到终点了
                    if v not in b :
                        b.add(v)
                        q.append((v,ans+1))
        return -1 
```