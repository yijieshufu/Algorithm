既然是要在 LeetCode 上提交，我们需要将代码封装在 `Solution` 类中。这道题是 **状态压缩 DP** 的经典应用，核心在于利用 `n <= 16` 这个极小的范围，用二进制位表示每个数字的使用状态。

### 题目考察类型

- **算法**：状态压缩 (Bitmask) + 记忆化搜索 (DFS)。
    
- **关键点**：判断是否能将总和 $S$ 均匀分成 $k$ 份，每份目标值为 $target = S / k$。
    

---

### 最优解思路

1. **基本剪枝**：如果总和不能被 $k$ 整除，或者数组中最大的数超过了 $target$，直接返回 `False`。
    
2. **排序优化**：对 `nums` 进行**降序排序**。大数字先占位可以极大地减少搜索树的分支数量。
    
3. **状态定义**：`dfs(mask, cur_sum)`。
    
    - `mask`：二进制位，第 $i$ 位为 $1$ 表示 `nums[i]` 已被使用。
        
    - `cur_sum`：当前正在构建的子集累加和。
        
4. **状态压缩逻辑**：如果 `cur_sum + nums[i] == target`，说明填满了一个子集，下一层递归的 `cur_sum` 重置为 $0$。
    

---

### Python 提交代码

```Python
from typing import List
from functools import lru_cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False
        target = s // k
        nums.sort(reverse=True) # 降序排序是核心剪枝
        if nums[0] > target: return False
        
        n = len(nums)

        @lru_cache(None)
        def dfs(mask, cur):
            # 所有数字都用完了，说明成功
            if mask == (1 << n) - 1:
                return True
            
            for i in range(n):
                # 状态检查：如果 nums[i] 已被使用，跳过
                if not (mask & (1 << i)):
                    # 剪枝：如果当前数字放进去超过了 target，跳过
                    # 由于 nums 是降序的，后续的数字可能更小，所以用 continue
                    if cur + nums[i] <= target:
                        # 核心转移：如果加完正好等于 target，则下一个 cur 重置为 0
                        next_cur = 0 if cur + nums[i] == target else cur + nums[i]
                        if dfs(mask | (1 << i), next_cur):
                            return True
                    else:
                        # 降序优化：如果当前的 nums[i] 已经太大了，
                        # 因为是降序，后面虽然可能有更小的，但为了严谨这里只对当前 i 剪枝
                        continue
            return False

        return dfs(0, 0)
```

[[LeetCode 698代码递归的逻辑]]

---

### 教练点拨：为什么这个代码能过？

- **状态冗余消除**：实际上，只要 `mask` 确定了，`cur` 的值其实是唯一的（即 `sum(mask中选中的数) % target`）。但在 Python 中为了代码直观，同时传入 `cur` 配合 `lru_cache` 依然非常高效。
    
- **时间复杂度**：$O(n \cdot 2^n)$。由于 $n=16$，$2^{16} = 65536$，乘上 $n$ 约为一百万次运算，这在 Python 3 的 $2$ 秒限制内绰绰有余。
    
- **空间复杂度**：$O(2^n)$，主要消耗在 `lru_cache` 的哈希表上。
    

