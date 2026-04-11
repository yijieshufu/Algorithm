# LC 217. 存在重复元素
给你一个整数数组 `nums`。如果任一值在数组中出现**至少两次**，返回 `true`；如果数组中每个元素互不相同，返回 `false`。

# 分析

set集合去重  
	通过长度来实现了 是否有重复的元素
# 代码

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```