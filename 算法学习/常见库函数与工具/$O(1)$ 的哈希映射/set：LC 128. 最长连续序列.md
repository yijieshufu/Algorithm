# LC 128. 最长连续序列
给定一个未排序的整数数组 `nums`，找出**数字连续**的最长序列（不要求序列元素在原数组中连续）的长度。  
要求时间复杂度为 $O(N)$。
# 分析
找到起点  
	v - 1 不在 说明 v 是起点  
	然后走下去就可以
# 代码

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        ans = 0 
        for v in a :
            if v - 1 not in a : # 找到起点
                cur = v + 1
                while cur in a : # 一种走
                    cur +=1
                ans = max(ans,cur - v )
        return ans 
```