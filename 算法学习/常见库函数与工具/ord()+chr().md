# 字符统计-真题
- **核心动作**：在由大写字母组成的字符串 $S$ 中，找出**出现次数最多**的字符；若有多个，按**字典序**依次输出。
- **数据边界**：$|S| \le 10^6$。必须实现 $O(N)$ 时间复杂度以避免超时（TLE）。

## 代码

```python
import sys
it = iter(sys.stdin.read().split())
s = next(it)
cnt = [0] * 26
for char in s:
    cnt[ord(char) - ord('A')] += 1  
mx = max(cnt)
ans = []
for i in range(26):
    if cnt[i] == mx:
        ans.append(chr(i + ord('A')))
print("".join(ans))
```

## 总结
```python
ans = ['A', 'B', 'C']

# 1. 空胶水（你的用法）
print("".join(ans))   # 输出: ABC

# 2. 空格胶水
print(" ".join(ans))  # 输出: A B C

# 3. 换行胶水（竞赛中常用于按行输出）
print("\n".join(ans)) 
# 输出:
# A
# B
# C

# 4. 酷炫胶水
print(" -> ".join(ans)) # 输出: A -> B -> C
```