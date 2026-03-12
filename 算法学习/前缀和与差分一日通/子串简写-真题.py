import sys

# 1. 极简 I/O 起手式
it = iter(sys.stdin.read().split())
k = int(next(it))
s = next(it)
c1 = next(it)
c2 = next(it)
n = len(s)
ans = 0
cnt = 0 # 记录当前 j 之前，满足长度限制的 c1 数量 [块 1]

# 2. 线性扫描 [块 2]
for j in range(n):
    # 计算当前结尾 j 对应的最远合法起点下标 i
    i = j - k + 1 
    if i >= 0:
        if s[i] == c1:
            cnt += 1 # 发现一个新的合法起点
    # 如果当前位是结尾字符，累加所有合法起点的贡献 [块 3]
    if s[j] == c2:
        ans += cnt

print(ans)