# 吊坠-真题
**【材料】 (Materials)**
- **对象**：$n$ 个长度为 $m$ 的环形字符串。
- **边权**：两个字符串的“最长公共子串”长度。由于是环形的，字符串可以旋转（改变起始位置）。
- **连接要求**：用 $n-1$ 条边将 $n$ 个字符串连成一个整体（即一棵树）。
- **规模**：$n \le 200, m \le 50$。  
**【条件】 (Constraints)**
- **环形匹配**：字符串 $A$ 和 $B$ 的边权是：在所有可能的旋转中，它们能达到的最大公共子串长度。
    - _逻辑转换_：这等价于求一个最长字符串 $P$，使得 $P$ 既是 $A+A$ 的子串，又是 $B+B$ 的子串，且 $|P| \le m$。
- **最大化**：需要总边权和最大。  
**【目的】 (Objective)**
- 寻找这棵树，使得 $n-1$ 条边的边权总和最大。
## 🧠 逻辑流：遇到了什么 $\rightarrow$ 想到什么
#### **1. 遇到“环形字符串匹配” $\rightarrow$ 想到“倍增法”**
- **分析**：将字符串 $s$ 复制一遍变成 $s+s$，那么所有的旋转情况产生的子串都会出现在这个倍增后的长字符串中。
- **决策**：预处理出每个字符串所有可能的环形子串，存入集合（Set）中，方便快速对比。
#### **2. 遇到“连接成整体且权值最大” $\rightarrow$ 想到“最大生成树”**
- **分析**：这是一个典型的最大生成树问题。
- **决策**：使用 **Kruskal 算法**。计算出所有 $n(n-1)/2$ 对字符串之间的边权，按权值从大到小排序，再用并查集进行合并。

首先计算公共子串  
	使用并查集 合并 连通分量  
	累计权重
## 代码

```python
import sys

it = iter(sys.stdin.read().split())
n,m= int(next(it)),int(next(it))
a = [next(it) for _ in range(n)]
b = []
f = list(range(n))
g = n
ans = 0
# 计算两两字符串的环形最长公共子串
for i in range(n):
  for j in range(i+1,n):
    w, s1 ,s2 = 0,a[i]+a[i],a[j]+a[j]
    for l in range(m,-1,-1): # 从m最长开始
      found = False
      for k in range(m): # 枚举从不同的起点
        if s1[k:k+l] in s2:
          w , found = l,True # 记录公共子串的长度
          break
        if found:break
      b.append((w,i,j)) # 记录到字符串之间的公共子串长度
b.sort(key = lambda x : x[0], reverse  = True) 
for w,u,v in b:
  if g == 1:break
  ra , rb = u,v
  while ra != f[ra]:f[ra]=f[f[ra]];ra = f[ra]
  while rb != f[rb]:f[rb]=f[f[rb]];rb = f[rb]
  if ra != rb: #合并
    f[ra] = rb;ans += w
    g-=1
print(ans)

```