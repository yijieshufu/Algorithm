# 哈希表的实现
给定一个集合与 $q$ 次操作，每次操作具体如下：  
`I x`：在集合中插入一个值为 $x$ 的数。  
`Q x`：查询 $x$ 是否在集合中出现过。
## 分析
**遇到“查询 $x$ 是否出现过”** $\rightarrow$ 想到需要**快速查找**。  
**遇到 $O(1)$ 查询** $\rightarrow$ 想到 **`set`（哈希表）** 或 **`dict`（字典）**
## 代码
```python
import sys 
it = iter(sys.stdin.read().split())
q = int(next(it))
a = set()
for _ in range(q):
  op = next(it);x = int(next(it))
  if op =="I":
    a.add(x)
  elif op =="Q":
    if x in a :
      print("Yes")
    else:print("No")
```
