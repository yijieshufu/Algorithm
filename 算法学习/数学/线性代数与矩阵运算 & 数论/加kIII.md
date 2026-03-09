
### 1. 题目背景与模板

**题目描述**：

给定 $t$ 组测试数据和一个全局正整数 $x$。每组数据给定初始正整数 $n$ 和操作次数 $k$。每次操作将 $n$ 的十进制每一位数字加上 $x$ 形成一个新数。求操作结束后整个数字的长度，结果对 $1000000007$ 取模。

**输入条件**：$1 \le t \le 10^4, 1 \le n \le 10^9, 1 \le k \le 10^9, 1 \le x \le 10^9$。

**所选题型**：矩阵快速幂（Matrix Exponentiation）

**通用模板代码**：

```Python
import sys; input=sys.stdin.read().split(); it=iter(input);
mod = 1000000007

# 核心算法：矩阵乘法
def mul(a, b, n):
    c = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for k in range(1, n+1):
            if not a[i][k]: continue
            for j in range(1, n+1):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c

# 核心算法：矩阵快速幂
def qpow(a, k, n):
    res = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1): res[i][i] = 1
    while k:
        if k & 1: res = mul(res, a, n)
        a = mul(a, a, n)
        k >>= 1
    return res

# 核心算法：纯函数封装
def solve():
    pass

# 主流程：处理 I/O
if input:
    pass
```

### 2. 题目与核心思路

- **逻辑总结**：全局 $x$ 固定，因此 $0 \sim 9$ 每个数字经过一次操作产生的新数字是固定的。构建 $10 \times 10$ 的状态转移矩阵 $M$。由于询问次数 $t$ 高达 $10^4$，不能每次都做完整的矩阵快速幂。通过预处理 $M$ 的 $2^0 \sim 2^{30}$ 次幂，在每次询问时，将 $n$ 转换为表示数位频次的 $1 \times 10$ 初始向量 $V$，利用 $k$ 的二进制位直接让 $V$ 乘以预处理好的矩阵，从而将 $O(N^3)$ 的矩阵乘法降维为 $O(N^2)$ 的向量乘法。
    
- **时空复杂度**：预处理矩阵时间 $O(30 \cdot 10^3)$，每次询问时间 $O(30 \cdot 10^2)$，总时间复杂度约 $3.2 \times 10^7$ 次运算，符合要求。空间复杂度 $O(30 \cdot 10^2)$ 用于存储 31 个矩阵，极低。
    

### 3. 我的盲点记录

- **矩阵的行与列映射**：一开始没搞懂数字演化怎么填入矩阵。实际上，矩阵的“列”代表演化前的旧数字，“行”代表演化后产生的新数字。例如 $5+12=17$，就是在第 6 列（代表数字 5）的第 2 行（代表数字 1）和第 8 行（代表数字 7）加上 1。
    
- **快速幂的底层逻辑**：理解了快速幂不只是对数字，对矩阵也是通过判断 `k & 1` 累乘结果，并利用 `a = mul(a, a, n)` 让底数自身不断平方“进化”来跳过不必要的计算。
    
- **向量乘矩阵的降维打击**：明白了在多组询问下，用 $1 \times 10$ 的行向量 $V$ 去乘预处理好的矩阵（$V \times M^k$），避免了高昂的矩阵间相乘，是本题不超时的绝对核心。
    

### 4. 最终范本代码
```Python
import sys; input=sys.stdin.read().split(); it=iter(input);
mod = 1000000007

def mul(a, b, n):
    c = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for k in range(1, n+1):
            if not a[i][k]: continue
            for j in range(1, n+1):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c

# 核心算法纯函数，接收数据并返回答案数组
def solve(t, x, qs):
    # -> 根据题目0-9数字转化规律，初始化10x10的基础转移矩阵修改了这里的逻辑
    m = [[0]*11 for _ in range(11)] 
    for j in range(10):
        s = str(j + x)
        for c in s:
            m[int(c) + 1][j + 1] += 1
            
    # -> 根据题目t=10^4优化，跳过qpow，改为预处理矩阵的2^p次幂修改了这里的逻辑
    pw = [m]
    for _ in range(30):
        pw.append(mul(pw[-1], pw[-1], 10))
        
    ans = []
    for n_s, k in qs:
        # -> 根据题目需求，将初始数字n_s的各个数位统计成1x10的状态向量修改了这里的逻辑
        v = [0]*11 
        for c in n_s:
            v[int(c) + 1] += 1
            
        p = 0
        while k > 0:
            # -> 根据题目优化要求，将原模板的矩阵乘法改为O(N^2)的向量乘矩阵修改了这里的逻辑
            if k & 1:
                nv = [0]*11
                mp = pw[p]
                for i in range(1, 11):
                    for jj in range(1, 11):
                        if v[jj] and mp[i][jj]:
                            nv[i] = (nv[i] + mp[i][jj] * v[jj]) % mod
                v = nv
            k >>= 1
            p += 1
            
        ans.append(str(sum(v) % mod))
    return ans

# 外部主流程只负责处理 I/O 并调用核心函数
if input:
    t = int(next(it))
    x = int(next(it))
    qs = []
    for _ in range(t):
        qs.append((next(it), int(next(it))))
    
    res = solve(t, x, qs)
    sys.stdout.write("\n".join(res) + "\n")
```