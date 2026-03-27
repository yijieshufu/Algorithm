# GCD
给定两个不同的正整数 $a$ 和 $b$，寻找一个**正整数** $k$，使得 $gcd(a+k, b+k)$ 的值达到最大。

如果满足最大值的 $k$ 有多个，输出其中最小的一个。
# 分析

公式表达：$\gcd(x, y) = \gcd(x, y - x)$。  
放在这道题里，就是：
$$
\gcd(a+k, b+k) = \gcd(a+k, (b+k) - (a+k)) = \gcd(a+k, b-a)
$$

**重点来了：**
- 不管你加多大的 $k$，右边的项 $b-a$ 是一个**固定不变的常数**。
- 既然是求 $\gcd(a+k, \text{常数})$，那么这个最大公约数**绝对不可能超过这个常数本身**。
- 我们的目标就是：让这个 $\gcd$ **等于**这个常数（设为 $D = b-a$）。

这道题的逻辑就是：
1. **差值** $D = |b-a|$ 是 $\gcd$ 的天花板。
2. 我们要让 $a+k$ 变成 $D$ 的倍数。
3. 利用取模运算 `a % D` 算出弟弟“多出了”多少，然后用 `D - 多出的` 算出要补多少。
## 代码

```python
import os
import sys
it=iter(sys.stdin.read().split())
a = int(next(it))
b = int(next(it))
if a > b: # b最大
  a,b=b,a
diff = b - a
rem = a % diff #  计算 a 距离上一个 D 的倍数多出了多少 (余数)
if rem == 0:
  print(diff)
else:
  print(diff-rem)
```
