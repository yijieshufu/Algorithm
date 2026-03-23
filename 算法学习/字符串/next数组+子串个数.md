# boarder
**【描述】 (Description)**  
给定一个字符串 $s$，计算该字符串最多是由多少个相同的子串重复拼接而成的。例如，`abcdabcd` 是由 `abcd` 重复 2 次组成，结果为 2；`aaaaa` 是由 `a` 重复 5 次组成，结果为 5。  
**【条件】 (Constraints)**
- 字符串长度 $1 \le |s| \le 10^6$。
- 必须是**相同**子串**完整**拼接，不能有剩余。
- 要求重复次数最大，即找**最短**的循环元。  
**【目的】 (Objective)**  
输出最大的重复次数 $n$。
## 分析
计算next数组  
	得到 最长相等前后缀长度 $M$。  
	这道题 : n - M 代表 向右拉 n-M个位置后  
		两个子串重合  
		如果 它能被 n 整除  
		那么 可以计算有多少个重复的子串了

## 代码
```python
import os
import sys

it = iter(sys.stdin.read().split())
s =next(it)
n = len(s)
f = [0]*(n) # next数组
j = 0
# 构建next数组
for i in range(1,n): # i不回头
  while j>0 and s[i]!=s[j]:
    j = f[j-1]  # j 回跳到上一次前后缀相同的地方
  if s[i] == s[j]:
    j+=1 # 找到相同的了 前后缀长度加一
  f[i] = j # 记录当前位 j

m = n-f[n-1]  # 下标从0开始的 最后一个是 n-1 记录了 最长相等前后缀长度 M
ans = n//m if n%m == 0 else 1 
print(ans)
```
