# 47. 全排列 II (Permutations II)
- **输入**：一个可包含**重复数字**的序列 `nums`（如 `[1, 1, 2]`）。
- **任务**：返回所有**不重复**的全排列。
- **数据范围**：$1 \le n \le 8$，数字范围 $[-10, 10]$。
# 分析
在 DFS 搜索过程中，同样的数字 `1` 出现两次，我们要区分两种情况：
- **情况 A（纵向）：** 第一个 `1` 在第一层，第二个 `1` 在第二层。
    - **例子**：路径是 `[1, 1, ...]`。
    - **性质**：这是“父子关系”。为了凑齐排列，我们**需要**这种情况。
- **情况 B（横向）：** 两个 `1` 都在尝试填入**同一个位置**。
    - **例子**：第一个 `1` 填入位置 0 搜完回溯了；现在第二个 `1` 也想填入位置 0 重新开一局。
    - **性质**：这是“兄弟关系”。由于数字一样，它们开启的“新战局”长得完全一样。
    - **结论**：这是**重复**的，必须拦截。
# 代码

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        nums.sort()
        used = [False] * (n+1)
        def dfs():
            if len(path) == n: # 达到满足的条件
                res.append(path[:])
                return 
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: # 最关键的代码
                    continue

                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return res
```