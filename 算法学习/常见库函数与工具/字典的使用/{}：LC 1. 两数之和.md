# LC 1. 两数之和
给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
# 分析

`enumerate` 给出 下标和值

不是直接使用加法  
	而是直接配对  
		配对成功 返回 坐标  
		不成功 那就放到 {} 中 等用
# 代码
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        g = {}
        for i,v in enumerate(nums):
            if target - v in g :
                return [g[target-v],i]
            g[v] = i
```
