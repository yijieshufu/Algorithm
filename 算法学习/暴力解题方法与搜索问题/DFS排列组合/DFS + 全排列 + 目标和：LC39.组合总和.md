# 39.组合总和
- **输入**：一个**无重复元素**的整数数组 `candidates` 和一个目标整数 `target`。
- **任务**：找出 `candidates` 中可以使数字和为 `target` 的所有**不同组合**。
- **规则**：`candidates` 中的同一个数字可以**无限制重复被选取**。
- **输出**：返回一个二维列表，包含所有满足条件的组合。

# 分析
#### ① 如何实现“无限重复选取”？
在全排列中，我们用 `dfs(depth + 1)` 走向下一层。  
在组合总和中，如果我们选了下标为 `i` 的数，下一层递归时，我们依然传入下标 `i`（而不是 `i + 1`）。  
这表示下一层依然可以从当前这个数开始选。
#### ② 如何保证组合“不重样”？
为了避免搜到 `[2, 2, 3]` 之后又搜到 `[3, 2, 2]`，我们要规定一个 **“只许前进，不许回头”** 的规则。
- **做法**：使用一个 `begin` 变量。每一层搜索只能从 `begin` 开始往后看，不能选 `begin` 之前的数。
#### ③ 剪枝优化（提升效率的关键）
如果我们将 `candidates` **先排序**，那么在循环中，如果发现 `当前数 > 剩余目标值`，那么它后面的数肯定也大，可以直接 `break` 掉这一层循环。
 # 代码
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        candidates.sort()
        def dfs(remain,begin):
            if remain == 0: # 出口
                res.append(path[:])
                return 
            for i in range(begin,n):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                dfs(remain-candidates[i],i) # 每次传入还剩下多少 可以重复使用 每次都可以用i
                path.pop()
        dfs(target,0)
        return res
```