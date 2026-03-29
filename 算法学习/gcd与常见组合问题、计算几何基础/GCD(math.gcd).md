# 221 公约数
在 $1$ 到 $2021$ 之间，找出有多少个数与 $2021$ 的最大公约数 $\gcd(x, 2021) > 1$
## 代码
```python
import math
ans = 0
for i in range(1, 2022):
    if math.gcd(i, 2021) > 1:
        ans += 1
print(ans)
```
