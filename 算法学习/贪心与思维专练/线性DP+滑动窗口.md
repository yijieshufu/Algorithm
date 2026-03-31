# 奇怪的数-真题
求长度为 $n$ 的正整数个数，满足以下条件：
1. **奇偶对齐**：第 1, 3, 5... 位必须填奇数 $\{1, 3, 5, 7, 9\}$；第 2, 4, 6... 位必须填偶数 $\{0, 2, 4, 6, 8\}$。
2. **和限制**：任意**连续 5 位**数字之和不能超过 $m$。
3. **结果**：对 $998244353$ 取模。
## 分析

## 代码
```python
import sys 
it = iter(sys.stdin.read().split())
n,m = int(next(it)),int(next(it))
mod = 998244353
f = {}
# 前四位 要合法
for a in [1,3,5,7,9]:
  for b in [0,2,4,6,8]:
    for c in [1,3,5,7,9]:
      for d in [0,2,4,6,8]:  
       f[(a,b,c,d)] = 1
# 开始第5位判断
for i in range(5,n+1):
  g= {}
  nums = [1,3,5,7,9] if i%2==1 else [0,2,4,6,8]
  for (a,b,c,d),count in f.items():
    for e in nums:
      if a+b+c+d+e<=m:
        state = (b,c,d,e)
        g[state] = (g.get(state,0)+count)%mod
  f = g
print(sum(f.values())%mod)
```