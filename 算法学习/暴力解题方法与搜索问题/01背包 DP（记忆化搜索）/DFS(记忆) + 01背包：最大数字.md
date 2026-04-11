# 最大数字-真题
给定一个正整数 $N$（最高 18 位），你可以对每一位进行两种操作：
1. **操作 1（加法）**：该位数字 $+1$。若当前是 $9$，加 $1$ 后变为 $0$。最多使用 $A$ 次。
2. **操作 2（减法）**：该位数字 $-1$。若当前是 $0$，减 $1$ 后变为 $9$。最多使用 $B$ 次。
- **目标**：在操作次数限制内，求出 $N$ 能变成的最大值。
# 分析
给定长度为 N 的数字，使用最多 A 次加法和 B 次减法，求能凑出的最大数值。  
**本质**：**从左到右的最优决策树**。每一个“数位”就是一个“物品”，你有两个背包（容量分别为 A 和 B），你要决定在这个数位上花多少 A 或 B，使得最终拼出的数字（总价值）最大。  
**核心状态**：`dfs(idx, a, b)`
- `idx`：当前算到了第几位。
- `a, b`：手里还剩多少次加法和减法。  
**边界条件的判断**：  
```python
if idx == length: return 0  # 走完了所有位，后面没有数值了
if (idx, a, b) in memo: return memo[(idx, a, b)] # 算过的直接拿来用（剪枝核心）
```
**决策分支（状态转移）**：
- **路线 1（用减法变 9）**：代价固定是 `d + 1`，前提是 `b >= d + 1`。
- **路线 2（用加法推高）**：代价是加到 9 或者把 `a` 耗光，花费 `min(a, 9 - d)`。
- **汇总**：`res = max(路线1, 路线2)`
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
  # 出口
  if idx == length:return 0 
  # 记忆
  state = (idx,a,b)
  if state in memo: return memo[state]
  
  d = nums[idx] # 取到当前的数
  res = 0 # 当前这边的最大值
  p10 = 10**(length - 1 - idx) # 当前位的权重  
  if b>=d+1: #可以减到9
    res=max(res,9*p10+dfs(idx+1,a,b-(d+1))) # 当前位的值 + 后面的值
  use_a = min(a,9-d) # 加到9 使用a的次数
  res = max(res,(d+use_a)*p10 +dfs(idx+1,a-use_a,b))
  
  # 记忆
  memo[state] = res
  return res
print(dfs(0,a_limit,b_limit))
```
