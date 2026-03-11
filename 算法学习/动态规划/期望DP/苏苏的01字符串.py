import sys

def solve():
    # 1. 竞赛级快速读取
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    n = int(next(iterator))
    s = next(iterator)
    
    # 2. 常量定义
    MOD = 10**9 + 7
    INV2 = 500000004 # (MOD + 1) // 2
    
    ans = 0 # 总期望贡献
    l = 0   # 当前结尾连续1的期望长度
    
    # 3. 线性扫描
    for c in s:
        if c == '1':
            # 增量: 2L + 1
            ans = (ans + 2 * l + 1) % MOD
            l = (l + 1) % MOD
            
        elif c == '0':
            l = 0
            # ans 不变
            
        else: # c == '?'
            # 期望增量: 0.5 * (2L + 1)
            term = (2 * l + 1) * INV2 % MOD
            ans = (ans + term) % MOD
            
            # 期望长度: 0.5 * (L + 1)
            l = (l + 1) * INV2 % MOD
            
    print(ans)

if __name__ == "__main__":
    solve()
