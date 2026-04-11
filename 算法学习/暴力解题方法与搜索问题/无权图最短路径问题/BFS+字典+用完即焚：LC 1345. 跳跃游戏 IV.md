# LC 1345. 跳跃游戏 IV
给你一个整数数组 `arr`，求从下标 `0` 跳到最后一个下标所需的**最少操作次数**。 跳跃规则：
1. `i + 1`
2. `i - 1`
3. 相同数值跳跃：跳到任何 `arr[i] == arr[j]` 的下标 `j`。
# 分析

依次处理列表的情况

值相同的边可以跳跃  
	用 字典来处理 好找边

防止 DFS 出不来
```python
del p[v_val] # # 彻底剪枝，防止重复扫描
```
并列走  
	值相等的情况  
	下标走两边的情况
# 代码

```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n ==1 :return 0
        # 列表 预处理 为 字典
        p = {}
        for i,v in enumerate(arr):
            if v not in p : p[v] = []
            p[v].append(i) # 建立相同值 有那些下标
        # 距离数组
        g = [-1] *(n) 
        g[0] = 0
        q = [0] # 从0出发
        h = 0
        while h<len(q):
            u = q[h]
            h += 1
            d = g[u] + 1
            # 值相等的情况
            v_val = arr[u]
            if v_val in p:
                for v in p[v_val]: # 跳跃v_val一样的边
                    if g[v] ==-1:
                        g[v] = d
                        q.append(v)
                del p[v_val] # # 彻底剪枝，防止重复扫描
            # 走相同的情况
            for v in(u+1,u-1):
                if 0<= v < n and g[v] ==-1:
                    g[v] = d
                    q.append(v)
            if g[n-1] != -1 :return g[n-1]
        return -1
```