# 冷热数据队列-真题
- **结构**：由两个子队列组成：热数据队列 $q_1$（长度 $n_1$）和冷数据队列 $q_2$（长度 $n_2$）。
- **访问逻辑**：
    1. **未命中**：如果 $p$ 不在 $q$ 中，将其插入 **$q_2$ 的首部**。
    2. **命中**：如果 $p$ 已在 $q_1$ 或 $q_2$ 中，将其移动至 **$q_1$ 的首部**。
- **淘汰与移动逻辑**：
    - **容量检查**：任何队列超过容量时，丢弃其**尾部**数据。
    - **级联移动**：当 $q_1$ 溢出时，被淘汰的尾部数据页，如果此时 **$q_2$ 未满**，则移动到 **$q_2$ 的首部**；如果 $q_2$ 已满，则直接丢弃。
# 分析
- `q1.move_to_end(p, last=False)` 移动到队头  
- 从 `q2` 移动到 `q1`：`del q2[p]` $\to$ `q1[p] = True` $\to$ `q1.move_to_end(p, last=False)`。    
- `q1` 满了：`out_p, _ = q1.popitem(last=True)`
- `q2` 满了：`q2.popitem(last=True)` 
# 代码
```python
import os
import sys
from collections import OrderedDict
it = iter(sys.stdin.read().split())
n1 = int(next(it))
n2 = int(next(it))
m = int(next(it))
q1 = OrderedDict()
q2 = OrderedDict()
for _ in range(m):
  p= next(it)
  if p in q1:
    q1.move_to_end(p,last = False) # 移到队头
  elif p in q2:
    del q2[p] # 删除
    q1[p] = True # 激活
    q1.move_to_end(p,last = False)
    if len(q1)>n1:
      out_p , _ = q1.popitem(last = True)
      if len(q2)<n2:
        q2[out_p] = True # 激活
        q2.move_to_end(out_p,last = False)
  else:# 都不在 移动到q2
    q2[p] = True
    q2.move_to_end(p,last = False)
    if len(q2)>n2:
      q2.popitem(last=True)
print(*(q1.keys())) if q1 else print()
print(*(q2.keys())) if q2 else print()
```
