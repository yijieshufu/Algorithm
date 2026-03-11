import sys

def solve():
    # ========== 极速读入模板 ==========
    it = iter(sys.stdin.read().split())  # 一次性读入，空格分割，生成迭代器
    try:
        n = int(next(it))                # 用 next() 逐个取数据
        m = int(next(it))
        # 下标从 1 开始，补 0 占位
        c = [0] + [int(next(it)) for _ in range(n)]
    except StopIteration:
        return  # 处理空输入
    
    # 特判：都不干活，赚 0 元
    if m == 0:
        print(0)
        return

    INF = 10**16  # 极小值代表"绝对不可能"
    
    # ========== 核心 DP 封装 ==========
    def run_dp(init_f0, init_f1):
        f0 = [-INF] * (m + 1)
        f1 = [-INF] * (m + 1)
        f0[0] = init_f0      # 0名额，不选第1个的状态
        if m >= 1:
            f1[1] = init_f1  # 1名额，选第1个的状态
            
        for i in range(2, n + 1):
            val = c[i]
            # 滚动数组：必须逆序！用昨天的状态推今天
            for j in range(m, -1, -1):
                # 今天摸鱼：继承昨天最高
                f0[j] = max(f0[j], f1[j])
                
                # 今天打工
                if j > 0:
                    f1[j] = max(f0[j-1], f1[j-1] + val)
                    
        return f0, f1

    # ========== 平行宇宙推演 ==========
    
    # 宇宙 A：1号不选（f0合法，f1非法）
    f0, f1 = run_dp(0, -INF)
    ans1 = max(f0[m], f1[m])

    # 宇宙 B：1号必选（f0非法，f1合法且工资欠着）
    f0, f1 = run_dp(-INF, 0)
    # n号不选：1号确实是新开工；n号选：首尾相连，补发c[1]
    ans2 = max(f0[m], f1[m] + c[1])

    print(max(ans1, ans2))

if __name__ == '__main__':
    solve()
