#review
# 题目描述
给定两个数 $a$ 和 $b$，计算 $a$ 的 $b$ 次方根（即 $a^{\frac{1}{b}}$），结果乘以 1000 后取整数部分。
# 分析
- **难度等级**：**入门级**。
- **高频程度**：**必备基础题**。虽然正式比赛很少单独考这种纯计算题，但“**幂运算**”和“**数据类型转换**”是处理复杂数学模型的基础。

本质考查 **幂运算**。在数学中，$\sqrt[b]{a}$ 等价于 $a$ 的 $\frac{1}{b}$ 次方。

# 代码
```python
import os
import sys
it = iter(sys.stdin.read().split())
a = float(next(it))
b = float(next(it))
print(int(a**(1/b)*1000))
```
# 笔记