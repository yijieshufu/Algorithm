

## 💡 归档总结：扩展欧几里得与乘法逆元

### 1. 题目背景与模板

- **题目描述**：给定 $a, b$，求 $ax \equiv 1 \pmod b$ 的最小正整数解 $x$。
    
- **输入条件**：$a, b$ 互质，数据量 $q \le 10^2$，$a, b \le 10^9$。
    
- **所选题型**：数论 - 扩展欧几里得算法（exGCD）。

**通用模板代码：**

```Python
import sys; input=sys.stdin.read().split(); it=iter(input);

# 核心算法：扩展欧几里得算法 (Extended Euclidean Algorithm)
# 返回值：(gcd, x, y) 满足 a*x + b*y = gcd(a, b)
def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x_prev, y_prev = exgcd(b, a % b)
    # 递归回溯更新当前的 x, y，基于公式 x = y', y = x' - (a//b)*y'
    x = y_prev
    y = x_prev - (a // b) * y_prev
    return d, x, y

# 核心算法：纯函数封装
def solve():
    pass

# 主流程：处理 I/O
if it:
    solve()
```

---

### 2. 题目与核心思路

- **逻辑总结**：
    
    1. 将同余方程 $ax \equiv 1 \pmod b$ 转化为不定方程 $ax + by = 1$。
        
    2. 利用 `exgcd` 递归求解出一组特解 $(x_0, y_0)$。
        
    3. 通过 `(x0 % b + b) % b` 将特解映射到最小正整数区间 $[0, b-1]$。
        
- **时空复杂度**：
    
    - **时间**：$O(q \log(\min(a, b)))$，每次查询消耗对数级时间。
        
    - **空间**：$O(\log(\min(a, b)))$，递归栈深度。

---

### 3. 我的盲点记录

- **疑问**：为什么 `exgcd` 能解出负数？
    
- **解答**：`exgcd` 求出的是直线 $ax + by = 1$ 上的**任意**一组整数坐标，不保证正负。
    
- **技巧**：在 Python 中，`x % b` 已经能处理部分负数情况，但为了保险（兼容其他语言习惯），统一使用 `(x % b + b) % b` 是最稳健的写法。

---

### 4. 最终范本代码

```Python
import sys; input=sys.stdin.read().split(); it=iter(input);

def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x_p, y_p = exgcd(b, a % b)
    x = y_p
    y = x_p - (a // b) * y_p
    return d, x, y

def solve():
    # -> 增加对 q 次查询的处理逻辑
    q = int(next(it))
    for _ in range(q):
        a = int(next(it))
        b = int(next(it))
        d, x, y = exgcd(a, b)
        # -> 根据题目“求 x 的值”且通常默认为最小正解，进行取模修正
        ans = (x % b + b) % b 
        sys.stdout.write(str(ans) + '\n')

if it:
    solve()
```

