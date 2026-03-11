import sys
from itertools import islice

# 使用 iter + next 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [0] + [int(next(it)) for _ in range(n)]

# f[i][j][0/1]: 打完区间[i,j]，最后停在左/右端点的最大得分
# 初始化为负无穷
INF = -10**18
f = [[[INF, INF] for _ in range(n + 2)] for _ in range(n + 2)]

# 初始化：从任意位置开始，获得全额分数，无移动代价
for i in range(1, n + 1):
    f[i][i][0] = f[i][i][1] = a[i]

# 区间DP：按长度从小到大扩展
for length in range(2, n + 1):           # 区间长度
    for i in range(1, n - length + 2):   # 左端点
        j = i + length - 1                # 右端点
        
        # 扩展到左端点 i
        # 从 [i+1,j] 的左端点来：同向，半额，移动1步
        val_from_left = f[i+1][j][0] + a[i] // 2 - 10
        # 从 [i+1,j] 的右端点来：反向，全额，移动(j-i)步
        val_from_right = f[i+1][j][1] + a[i] - (j - i) * 10
        
        if length == 2:  # 第一次移动，无历史方向，按全额
            f[i][j][0] = f[i+1][j][1] + a[i] - 10
        else:
            f[i][j][0] = max(val_from_left, val_from_right)
        
        # 扩展到右端点 j
        # 从 [i,j-1] 的右端点来：同向，半额，移动1步
        val_from_right2 = f[i][j-1][1] + a[j] // 2 - 10
        # 从 [i,j-1] 的左端点来：反向，全额，移动(j-i)步
        val_from_left2 = f[i][j-1][0] + a[j] - (j - i) * 10
        
        if length == 2:  # 第一次移动，无历史方向，按全额
            f[i][j][1] = f[i][j-1][0] + a[j] - 10
        else:
            f[i][j][1] = max(val_from_right2, val_from_left2)

# 答案：打完所有地鼠，停在左端点或右端点的最大值
print(max(f[1][n][0], f[1][n][1]))
