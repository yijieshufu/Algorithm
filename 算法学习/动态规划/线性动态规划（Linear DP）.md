# 线性动态规划（Linear DP）中的组合计数问题

## 基础代码

```Python
import sys

# 建议使用 sys.stdin.read().split() 快速读入
def solve():
    data = sys.stdin.read().split()
    if not data: return
    n, k = map(int, data)
    MOD = 10**9 + 7
    
    # f[i] 表示长度为 i 时的总方案数
    # 初始化 f[0] = 1 表示空序列也是一种合法方案
    f = [0] * (n + 1)
    f[0] = 1
    
    for i in range(1, n + 1):
        # 不选第 i 位
        f[i] = f[i-1]
        
        # 选第 i 位
        if i - k - 1 >= 0:
            f[i] = (f[i] + f[i-k-1]) % MOD
        else:
            # 当 i 较小时，选了第 i 位，前面只能全为空，贡献 1 种方案
            f[i] = (f[i] + 1) % MOD
            
    print(f[n])

solve()
```

## 变体 

## 题目

 [[动态规划的基础/安全序列]]  
[[动态规划的基础/破损的楼梯]]
