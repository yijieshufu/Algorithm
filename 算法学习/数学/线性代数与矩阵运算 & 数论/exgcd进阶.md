
### 题目背景与模板

**题目描述：** 给定长度为 $n$ 的数组 $a$，选择非负整数 $s, d$，使每一项 $a[k]$ 变为 $a[k] + s + k \cdot d$ ($k \in [1, n]$)，求数组总和对 $m$ 取模后的最小值。

**输入条件：$n \le 10^5, m \le 10^9$**。

**题型：** 数论 / 裴蜀定理应用。

```Python
import sys; input=sys.stdin.read().split(); it=iter(input);

# 核心算法：欧几里得算法模板
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 核心算法：纯函数封装
def solve():
    # 待填充：逻辑推导见下方最终范本
    pass

# 主流程：处理 I/O
if it:
    solve()
```

---

### 题目与核心思路

**逻辑总结：**

1. **公式推导**：总和 $S_{new} = \sum a_i + \sum_{k=1}^n (s + kd) = S_{orig} + n \cdot s + \frac{n(n+1)}{2} \cdot d$。
    
2. **变量简化**：令 $A = n, B = \frac{n(n+1)}{2}$，目标是最小化 $(S_{orig} + A \cdot s + B \cdot d) \pmod m$。
    
3. **裴蜀定理**：在模 $m$ 意义下，线性组合 $As + Bd \pmod m$ 能凑出的最小正整数步长是 $g = \gcd(A, B, m)$。
    
4. **最终结论**：原和 $S_{orig}$ 加上任意个 $g$ 后对 $m$ 取模的最小值，等价于 $S_{orig} \pmod g$。

**时空复杂度：**

- 时间复杂度：$O(n + \log m)$，主要是遍历一次数组求和及一次 $\gcd$ 计算。
    
- 空间复杂度：$O(n)$，取决于输入读取（或 $O(1)$ 如果流式处理）。

---

### 我的盲点记录

- **初识困惑**：题目描述中的 $s + k \cdot d$ 容易误导去思考每个元素的变化，实际上求“总和”时应该先进行整体求和公式化简。
    
- **非负约束**：虽然 $s, d \ge 0$，但在模运算的大循环下，只要步数足够多，正向增加等价于负向减少，因此直接套用 $\gcd$ 结论成立。

---

### 最终范本代码

```Python
import sys; input=sys.stdin.read().split(); it=iter(input);

# 核心算法：欧几里得算法
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    if not it: return
    n = int(next(it))
    m = int(next(it))
    
    # 1. 极简命名符合规范：s 为原数组总和
    s = 0
    for _ in range(n):
        s += int(next(it))
        
    # 2. 根据推导得出 s 和 d 的系数
    # c1: s 的系数是 n 个 s
    # c2: d 的系数是 1+2+...+n = n*(n+1)//2
    c1 = n
    c2 = n * (n + 1) // 2
    
    # 3. 计算步长 g = gcd(c1, c2, m) -> 裴蜀定理核心修改
    g = gcd(c1, gcd(c2, m))
    
    # 4. 输出最小模数结果 -> 逻辑推导：(s + k*g) % m 的最小值即为 s % g
    print(s % g)

if it:
    solve()
```

