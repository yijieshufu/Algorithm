import sys

# 初始点坐标 [块 1]
pts = [(0, 0), (2020, 11), (11, 14), (2000, 2000)]
t = 2020
ans = 0

# 确定扫描边界：min_coord - t 到 max_coord + t [块 1]
x_range = range(-2020, 2020 + 2020 + 1)
y_range = range(-2020, 2000 + 2020 + 1)

# 暴力枚举格点 [块 2 & 3]
for x in x_range:
    for y in y_range:
        # 只要满足任意一个初始点的曼哈顿距离约束即可
        for px, py in pts:
            if abs(x - px) + abs(y - py) <= t:
                ans += 1
                break # 只要变黑就停止检查其他点，优化性能

print(ans) # 赛场直接填结果