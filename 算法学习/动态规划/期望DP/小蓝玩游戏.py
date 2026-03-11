import sys

def solve():
    # 极速读取
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    n = int(next(it))
    m = int(next(it))
    
    # f[i][j] 初始化为 0
    # 维度 (n+1) * (m+1)
    f = [[0.0] * (m + 1) for _ in range(n + 1)]
    nm = n * m
    
    # 逆向推导：从 (n,m) 到 (0,0)
    for i in range(n, -1, -1):
        cur_row = f[i]
        next_row = f[i+1] if i < n else None
        ni = n - i
        
        for j in range(m, -1, -1):
            # 目标状态
            if i == n and j == m:
                continue
            
            mj = m - j
            
            if i == n:
                # 仅需集齐阵营：1D 模型
                cur_row[j] = cur_row[j+1] + m / mj
            elif j == m:
                # 仅需集齐职业：1D 模型
                cur_row[j] = next_row[j] + n / ni
            else:
                # 2D 模型公式推导结果
                # 分子
                numerator = (
                    nm + 
                    ni * mj * next_row[j+1] + 
                    ni * j * next_row[j] + 
                    i * mj * cur_row[j+1]
                )
                # 分母 (1 - P_stay) * nm
                denominator = nm - i * j
                cur_row[j] = numerator / denominator
                
    print(f"{f[0][0]:.4f}")

if __name__ == "__main__":
    solve()
