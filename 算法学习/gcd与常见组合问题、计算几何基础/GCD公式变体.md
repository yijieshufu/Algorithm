# CF1458A Row GCD
## 题目描述
给定两个正整数序列 $a_1, \ldots, a_n$ 和 $b_1, \ldots, b_m$。

对于每一个 $j = 1, \ldots, m$，求 $\gcd(a_1 + b_j, \ldots, a_n + b_j)$ 的值。
# 分析
## **核心逻辑：从“动态”中寻找“不动点”**
我们要算的是：$\gcd(a_1 + b_j, a_2 + b_j, \dots, a_n + b_j)$。  
根据 GCD 的性质，我们可以把第一项作为“基准”，让**后面所有的项都减去第一项**：  
$$\gcd(x_1, x_2, x_3, \dots) = \gcd(x_1, x_2 - x_1, x_3 - x_1, \dots)$$  
带入本题：  
$$\gcd(a_1 + b_j, (a_2 + b_j) - (a_1 + b_j), (a_3 + b_j) - (a_1 + b_j), \dots)$$  
$$= \gcd(a_1 + b_j, a_2 - a_1, a_3 - a_1, \dots, a_n - a_1)$$

**惊人的发现：**
- **第一项 $a_1 + b_j$**：随 $b_j$ 变化而变化。
- **后续项 $a_i - a_1$**：完全不随 $b_j$ 变化！它们是**固定不变**的常数。
## **解题步骤**
1. **预处理差值 GCD**：先算出 $G = \gcd(|a_2 - a_1|, |a_3 - a_1|, \dots, |a_n - a_1|)$。
2. **处理特殊情况**：如果 $n=1$，则没有差值，答案直接就是 $a_1 + b_j$。
3. **单次查询**：对于每个 $b_j$，答案就是 $\gcd(a_1 + b_j, G)$。
## 代码

```python
import sys
from math import gcd

it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a = [int(next(it)) for _ in range(n)]
b = [int(next(it)) for _ in range(m)]

# 2. 边界与预处理
# 计算所有 a[i]-a[0] 的公约数 G
g_diff = 0
for i in range(1, n):
    g_diff = gcd(g_diff, abs(a[i] - a[0]))

ans = []
for x in b:
    ans.append(str(gcd(a[0] + x, g_diff)))

# 4. 答案输出
print(" ".join(ans) + "\n")
```