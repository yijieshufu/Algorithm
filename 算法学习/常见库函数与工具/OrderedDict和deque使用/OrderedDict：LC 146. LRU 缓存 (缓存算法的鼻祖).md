# 题目
设计一个数据结构，满足：
1. `get(k)`：如果 `k` 存在，返回其值并将该数据设为“最新访问”；否则返回 -1。
2. `put(k, v)`：如果 `k` 已存在，更新值并设为“最新”；若不存在且容量满，淘汰“最久未访问”的数据。
3. **硬性要求**：两个操作的时间复杂度必须均为 $O(1)$。
# 分析
时间复杂度是O(1) `OrderedDict`  
队头是最久的  
队尾是最新的
# 代码
```python
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.n = capacity

    def get(self, key: int) -> int:
        if k not in self.d:return -1
        self.d.move_to_end(k) # 移动到队尾
        return self.d[k]

    def put(self, key: int, value: int) -> None:
        if k in self.d: self.d.move_to_end(k) # 先移动到队尾都
        self.d[k] = v 
        if len(self.d) > self.n:
            self.d.popitem(last = False) # 弹出 队头
```