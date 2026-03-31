# 最大数字-真题
给定一个正整数 $N$（最高 18 位），你可以对每一位进行两种操作：
1. **操作 1（加法）**：该位数字 $+1$。若当前是 $9$，加 $1$ 后变为 $0$。最多使用 $A$ 次。
2. **操作 2（减法）**：该位数字 $-1$。若当前是 $0$，减 $1$ 后变为 $9$。最多使用 $B$ 次。
- **目标**：在操作次数限制内，求出 $N$ 能变成的最大值。
# 分析
- **高位优先原则（贪心）**：  
    要使整体数值最大，最高位的权重最高。我们必须从左往右（从高位到低位）尽可能让数字变大，最好能变成 $9$。
- **变 9 的两种策略**：  
    对于某一位数字 $d$：
    - **通过加法变 9**：需要消耗 $9 - d$ 次操作 1。前提是剩余的 $A \ge 9 - d$。
    - **通过减法变 9**：需要消耗 $d + 1$ 次操作 2（即 $d \to 0 \to 9$）。前提是剩余的 $B \ge d + 1$。
- **决策分支**：  
    在每一位，我们面临选择：
    - **分支 A**：如果 $B$ 够用，直接把这一位减到 $9$。
    - **分支 B**：使用剩余的 $A$ 尽可能把这一位加高（最高加到 $9$）。
- **搜索空间**：  
    数字长度最多 18 位，$A, B$ 最大 100。状态 $(idx, a, b)$ 总量约为 $18 \times 100 \times 100 = 1.8 \times 10^5$，使用递归配合记忆化可以轻松通过。
## 代码
```python
import sys

# 设置递归深度防止溢出
sys.setrecursionlimit(2000)

# 统一高效输入
it = iter(sys.stdin.read().split())
s = next(it)
a_limit = int(next(it))
b_limit = int(next(it))

nums = [int(c) for c in s]
length = len(nums)
memo = {}  
# 从左向右开始 调整数字
def dfs(idx,a,b):
  if idx == length:return 0 
  state = (idx,a,b)
  if state in memo: return memo[state]
  d = nums[idx] # 取到当前的数
  res = 0 # 当前这边的最大值
  p10 = 10**(length - 1 - idx) # 当前位的权重      
  if b>=d+1: #可以减到9
    res=max(res,9*p10+dfs(idx+1,a,b-(d+1))) # 当前位的值 + 后面的值
  use_a = min(a,9-d) # 加到9 使用a的次数
  res = max(res,(d+use_a)*p10 +dfs(idx+1,a-use_a,b))
  memo[state] = res
  return res
print(dfs(0,a_limit,b_limit))
```
