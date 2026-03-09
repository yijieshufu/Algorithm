import sys

# 1. 蓝桥标准快速 I/O
it = iter(sys.stdin.read().split())
s1 = next(it)
s2 = next(it)
n = len(s1)
# 2. 定位范围 [L, R]
L, R = -1, -1  # L,R 代表的列
for i in range(n):
    if s1[i] == '#' or s2[i] == '#':
        if L == -1: L = i
        R = i

# 特判：河床没检测器
if L == -1:
    print(0)
    exit()

# 当前L列 都有的 话 就不用新增 如果f1没有 就要花费1 来满足 联通性
f0 = 0 if s1[L] == '#' else 1
f1 = 0 if s2[L] == '#' else 1

for i in range(L + 1, R + 1): # 从下一列开始
    # 当前格子如果是 '.' 则花费 c 为 1，如果是 '#' 则为 0
    c0 = 1 if s1[i] == '.' else 0
    c1 = 1 if s2[i] == '.' else 0
    # 暂存上一轮状态
    p0, p1 = f0, f1
    f0 = min(p0 + c0, p1 + c1 + c0) # 直接走 ，从下面走上来
    f1 = min(p1 + c1, p0 + c0 + c1) # 直接走 ，从上面走下来
    if s1[i] == '#' and s2[i] == '#':
        f0 = f1 = min(f0, f1) # 相当于 都不话费 那就取这两个的最小值
# 5. 输出最终最少增加数量
print(min(f0, f1))