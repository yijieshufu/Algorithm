# 题目
写一个 `RecentCounter` 类来计算最近的请求。  
它只有一个方法 `ping(t)`，参数 `t` 代表当前时间戳（毫秒）。  
返回在 `[t-3000, t]` 范围内的所有请求次数。  
保证每次调用 `ping` 的 `t` 都是严格递增的。
# 分析
先进先出 `deque`  
`append` 在队尾加  
`popleft()` 在队头删除
# 代码
```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)
```