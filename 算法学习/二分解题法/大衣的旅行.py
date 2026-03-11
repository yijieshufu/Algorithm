import sys
# 优化 I/O
it = iter(sys.stdin.read().split())
T_cases = int(next(it))
for _ in range(T_cases):
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))

    grid = []
    total_sum = 0
    for i in range(N):
        row = [int(next(it)) for _ in range(M)]
        grid.append(row) # 一行行存储
        total_sum += sum(row)

    # 基础可行性判定
    if total_sum < K + 1: #total_sum:总的容量
        print("-1")
        continue

    # 预处理二维前缀和
    S = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            S[i][j] = grid[i - 1][j - 1] + S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] #注意grid的下标

    def check(d):
        # 检查半径 d 是否能容纳 K+1 人
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if grid[i - 1][j - 1] > 0:  # 老师入住的房间必须有容量
                    r1, c1 = max(1, i - d), max(1, j - d)
                    r2, c2 = min(N, i + d), min(M, j + d) # 矩形的区域
                    if S[r2][c2] - S[r1 - 1][c2] - S[r2][c1 - 1] + S[r1 - 1][c1 - 1] >= K + 1:
                        return True
        return False
    # 二分查找最小距离 d
    low, high = 0, max(N, M)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
