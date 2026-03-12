import sys

# [块 1: 极简输入流与分类]
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a = [int(next(it)) for _ in range(n)]
# 分离正负并排序（存储绝对值以便计算）
neg = sorted([-x for x in a if x < 0])
pos = sorted([x for x in a if x >= 0])
ans = 0
j = len(pos) # 当前
# [块 3: 双指针线性扫描]
# i 表示选取负半轴矿洞的数量，j 表示正半轴（含0）的数量
for i in range(len(neg) + 1): 
    L = neg[i-1] if i > 0 else 0 # 块 1: 左边界距离
    if L > m: break
    while j > 0:
        R = pos[j-1] # 块 1: 右边界距离
        # [块 2: 核心距离推导]
        dist = min(2 * L + R, 2 * R + L)
        if dist <= m: break
        j -= 1 # 距离超标，右端点左移  # 此时 dist是大于m的
    ans = max(ans, i + j) # 更新最大矿石数
print(ans)