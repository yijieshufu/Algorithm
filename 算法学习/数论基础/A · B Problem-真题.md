# [A · B Problem-真题](https://www.lanqiao.cn/problems/20535/learning/?page=1&first_category_id=1&name=A%20%C2%B7%20B%20Problem)
设有四个正整数 $X_A, Y_A, X_B, Y_B$，它们分别构成两个二维向量 $\vec{A}(X_A, Y_A)$ 和 $\vec{B}(X_B, Y_B)$。给定一个正整数 $L$，求满足以下条件的四元组 $(X_A, Y_A, X_B, Y_B)$ 的不同取值数量：
1. $X_A, Y_A, X_B, Y_B$ 均为**正整数**；
2. $\vec{A} \cdot \vec{B} \le L$。  
其中 $\vec{A} \cdot \vec{B}$ 表示向量的内积，即：  
$$X_A \cdot X_B + Y_A \cdot Y_B \le L$$
## 分析
### 1. 数学建模
题目要求 $X_A \cdot X_B + Y_A \cdot Y_B \le L$。  
设 $u = X_A \cdot X_B$，$v = Y_A \cdot Y_B$。  
原式变为：$u + v \le L$，且 $u, v \ge 1$。  
对于一个固定的 $u$，有多少对正整数 $(X_A, X_B)$ 满足 $X_A \cdot X_B = u$ 呢？  
答案就是 $u$ 的**约数个数**，记作 $d(u)$。  
同理，满足 $Y_A \cdot Y_B = v$ 的对数就是 $d(v)$。
### 2. 公式推导
我们要计算的总数就是：  
$$\sum_{u=1}^{L-1} \sum_{v=1}^{L-u} d(u) \cdot d(v)$$  
为了提高效率，我们令 $g(k) = \sum_{i=1}^k d(i)$，即约数个数的前缀和。  
那么公式可以简化为：  
$$\sum_{u=1}^{L-1} d(u) \cdot g(L-u)$$
### 3. 算法实现
- **计算 $d(i)$**：使用类似埃氏筛的方法，枚举每个数 $i$，将其作为约数贡献给它的倍数 $i, 2i, 3i \dots$。时间复杂度 $O(L \log L)$。
- **前缀和 $g(i)$**：线性扫描一遍 $d(i)$ 即可。
- **最终求和**：遍历 $u$ 从 $1$ 到 $L-1$。
## 代码
```python
import os
import sys
it = iter(sys.stdin.read().split())
L = int(next(it))
if L < 2:print(0)
else:
  # 计算约数的个数
  d = [0]*(L+1)
  for i in range(1,L+1):
    for j in range(i,L+1,i):
      d[j]+=1
  # 计算约数前缀的个数
  G = [0]*(L+1)
  for i in range(1,L+1):
    G[i]=G[i-1]+d[i]
  ans = 0
  for s in range(1,L):
    ans += d[s] * G[L - s]
  print(ans)
```
