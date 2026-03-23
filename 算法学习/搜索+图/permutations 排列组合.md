# 串变换
**【材料】 (Materials)**
- **基础数据**：两个长度为 $n$ 的数字字符串 $S$ 和 $T$。
- **操作池**：共有 $k$ 个可选操作。
    - 类型 1：单位加法模 10 ($S_x = (S_x + v) \mod 10$)。
    - 类型 2：交换位置 ($S_x, S_y$ 互换)。
- **规模**：$n \le 10$，$k \le 7$。  
**【条件】 (Constraints)**
- **次数限制**：每个操作最多只能执行**一次**。
- **顺序自由**：可以挑出任意个操作，以**任意顺序**执行。
- **关键点**：由于交换操作和加法操作不满足交换律（顺序不同结果不同），必须考虑**排列**。  
**【目的】 (Objective)**
- 判断是否存在一种操作序列，使得 $S$ 串变为 $T$ 串。输出 `Yes` 或 `No`。
## 分析
直接暴力 操作序列  
	采用permutations 得到排列组合
## 代码
```python
import sys
from itertools import permutations
it =iter(sys.stdin.read().split())
n = int(next(it))
s = list(map(int,next(it))) # 将字符串转化为列表
t = list(map(int,next(it)))
k = int(next(it))
ops = []
for _ in range(k):
  op = int(next(it))
  x = int(next(it))
  y = int(next(it))
  ops.append((op,x,y))
ans = "No"
for r in range(k): # 选r个
  for p in permutations(range(k),r): # p 排列组合序列
    g = s[:] # 复制
    for i in p:
      op,x,y=ops[i]
      if op ==1:
        g[x]=(g[x]+y)%10
      elif op ==2:
        g[x],g[y]=g[y],g[x]
    if g == t: ans = "Yes" # 找到了一种序列是可以的了
  if ans == "Yes":break #结束序列的判断 如果有就可以了
print(ans)
```

**`next(it)`**：从输入里把那个数字串（如 `"01012"`）搬进来。  
**`map(int, ...)`**：把里面的每个字符直接变成整数  
`list()` 转化为列表  
如果 `s=next(it)` 得到了字符串 但是 `s[i]`只能读取 不能赋值修改  
	要修改 必须变为 `list(next(it))` 这样才可以  
	如果要求是 数组的话：`list(map(int,next(it)))`