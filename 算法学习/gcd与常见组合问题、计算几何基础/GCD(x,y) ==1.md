# 题目描述
求 $1$ 到 $2020$ 之间，分子分母互质（最大公约数为 $1$）的分数个数。
# 分析

```python
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a
```
## 代码

```python
import os
import sys
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a
ans=0
for i in range(1,2021):
  for j in range(1,2021):
    if gcd(i,j) == 1:
      ans+=1
print(ans)
```
