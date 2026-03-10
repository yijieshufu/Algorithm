

### 题目背景与模板

**题目描述**：给定 $n$ 个数的初始序列，随后进行 $k$ 次插入。每次插入后，需实时输出当前所有数中第 $n$ 大的数。

**输入条件**：$1 \le n \le 10^4, 1 \le k \le 10^5$。

**所选题型**：动态维护第 $K$ 大值（固定容量小根堆）。

**核心算法：固定容量小根堆模板**
```Python
import heapq

# 核心算法：维护前 n 名精英，堆顶即为第 n 大（精英里的最弱者）
def maintain_top_n(h, val):
    # -> 如果新数比当前第 n 大还要大，说明它进入了前 n 名
    if val > h[0]:
        heapq.heapreplace(h, val) # 踢出旧的第 n 大，加入新精英并重排
    return h[0]
```

---

### 题目与核心思路

- **逻辑总结**：
    
    1. **精英俱乐部**：第 $n$ 大意味着我们需要关注当前最大的 $n$ 个数。
        
    2. **小根堆守门**：用一个小根堆存储这 $n$ 个数。由于是小根堆，堆顶 `h[0]` 必然是这 $n$ 个数中最小的，也就是全局第 $n$ 大。
        
    3. **动态更新**：新元素只有比“守门员”强时才能入堆，并踢走旧的守门员。
        
- **复杂度分析**：
    
    - **时间**：$O(n + k \log n)$，初始化堆 $O(n)$，之后 $k$ 次操作每次 $O(\log n)$。
        
    - **空间**：$O(n)$，堆的大小始终维持在 $n$。

---

### 我的盲点记录

- **疑问**：为什么代码中没有看到 `heapq.heappush`？
    
- **解答**：因为本题初始就有 $n$ 个数，且后续我们要找的依然是第 $n$ 大。这意味着“精英俱乐部”的名额始终是满的。使用 `heapq.heapreplace` 可以一步完成“踢出最弱者”和“加入强者”的操作，比先 `pop` 后 `push` 更高效。

---

### 最终范本代码

```Python
import sys
import heapq

# 针对 Python 3.7.3 规范：极简 I/O
input = sys.stdin.read().split()
it = iter(input)

# 核心算法：固定容量小根堆模板
def maintain_top_n(h, val):
    # -> 只有当新数 val 大于堆顶（当前第 n 大）时才需要替换
    if val > h[0]:
        heapq.heapreplace(h, val)
    return h[0]

# 核心算法：纯函数封装
def solve():
    if not it: return
    n = int(next(it))
    k = int(next(it))
    
    # 1-indexed 逻辑：虽然 a 是列表，但我们读入 n 个数作为初始堆
    a = [0] * (n + 1)
    h = []
    for i in range(1, n + 1):
        h.append(int(next(it)))
    
    # 初始化堆：O(n)
    heapq.heapify(h)
    
    ans = []
    # 处理 k 次插入
    for i in range(1, k + 1):
        x = int(next(it))
        # -> 直接调用模板函数，传入当前堆和新值
        res = maintain_top_n(h, x)
        ans.append(res)
    
    # 批量输出
    print(*(ans))

# 主流程：处理 I/O 并调用
if __name__ == "__main__":
    if input:
        solve()
```
