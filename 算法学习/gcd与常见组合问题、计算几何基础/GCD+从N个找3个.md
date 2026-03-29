# 宝石组合
在森林里有 $N$ 枚宝石，第 $i$ 枚宝石的“闪亮度”为 $H_i$。小蓝需要从中选出三枚宝石，其组合的“精美程度” $S$ 由以下公式计算：  
$$S = H_a H_b H_c \cdot \frac{\text{LCM}(H_a, H_b, H_c)}{\text{LCM}(H_a, H_b) \cdot \text{LCM}(H_a, H_c) \cdot \text{LCM}(H_b, H_c)}$$  
目标是找到使 $S$ **最大化**的三枚宝石。若 $S$ 相同，则选择三者升序排列后**字典序最小**的方案。
# 分析
[[GCD知识的本质]]

[[宝石组合复杂公式的化简]]  
这个复杂的公式其实可以简化为一个非常简洁的形式。  
利用性质 $\text{LCM}(x, y) = \frac{xy}{\text{GCD}(x, y)}$ 以及三元素的 LCM 公式，经过代数化简可得：  
也就是说，**精美程度 $S$ 就是三枚宝石闪亮度的最大公约数。**

**解题步骤：**
1. **统计频率**：用一个数组 $f$ 记录每个数值出现的次数。
2. **枚举 GCD**：从可能的最大闪亮度 $m$ 开始**向下枚举**每一个可能的公约数 $g$。
3. **寻找倍数**：对于当前的 $g$，检查它的倍数（$g, 2g, 3g, \dots$）在原数据中是否存在。
4. **计数与停止**：如果 $g$ 的倍数总数（计入重复数值）大于等于 3，那么这个 $g$ 就是能达到的最大 $S$。
5. **字典序优化**：由于我们要找字典序最小的方案，在枚举 $g$ 的倍数时，应从小到大选取前三个存在的数值。

# 代码

```python
import sys
it = iter(sys.stdin.read().split())

# 1.变量
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
m = max(a)
f = [0] * (m + 1)
ans = []

# 2.边界
for b in a:
    f[b] += 1

# 3.操作
# 从最大可能的GCD开始枚举
for g in range(m, 0, -1):
    a = []
    # 从小到大找g的倍数，确保字典序最小
    for b in range(g, m + 1, g):
        if f[b] > 0:
            # 一个数可能出现多次，取前三个即可
            for _ in range(min(f[b], 3 - len(a))):
                a.append(b)
        if len(a) >= 3:
            break
    if len(a) >= 3:
        ans = sorted(a)
        break

# 4.答案
print(*(ans))
```
