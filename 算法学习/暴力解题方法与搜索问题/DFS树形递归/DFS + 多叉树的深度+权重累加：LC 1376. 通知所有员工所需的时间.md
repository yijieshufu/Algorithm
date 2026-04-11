# LC 1376. 通知所有员工所需的时间
- **输入**：
    - `n`：员工总数。
    - `headID`：总负责人的 ID。
    - `manager` 数组：`manager[i]` 是员工 `i` 的直属老板。
    - `informTime` 数组：`informTime[i]` 是老板 `i` 通知他**所有直属下属**所需的时间。
- **规则**：老板是“群发”消息的，下属们会**同时**收到消息，然后各自继续往下传。
- **任务**：求出所有员工都收到消息所需的**总分钟数**。

# 分析 

题目给的 `manager` 数组是“下属指向老板”（子指父）。  
	但消息是从上往下传的，所以我们必须先建一个图/树，把它变成 **“老板指向下属”** 的字典或数组列表。

因为老板是“群发”消息，所以同一层级的下属是**并发**工作的。  
	整个公司完全收到消息的时间，取决于**耗时最长的那条汇报线（木桶效应的短板/树的最长路径）**。  
	- **状态转移逻辑**： `我负责的部门总耗时 = 我自己发邮件的时间 (informTime) + max(所有直属下属部门的总耗时)`
# 代码
```python
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = [[] for _ in range(n)]
        # 每个老板的所有的员工
        for i in range(n):
            if manager[i]!= -1:
                g[manager[i]].append(i)
        def dfs(u): # 编号
            if not g[u]:
                return 0 
            mx = 0
            for v in g[u]: # 找到自己的手下
                res = dfs(v) # 计算手下要的时间
                if res > mx : mx = res 
            return informTime[u] + mx # 自己传播的时间 + 手下的时间
        return dfs(headID) # 从大boss开始
```
