import sys
import math
# 精度控制值
EPS = 1e-9

class Circle:
    def __init__(self, x, y, r):
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)

# 1. 计算两点距离（圆心距）
def get_dist(c1, c2):
    return math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)
# 2. 核心判定函数
def check_relationship(c1, c2):
    d = get_dist(c1, c2)
    s = c1.r + c2.r          # 半径和
    diff = abs(c1.r - c2.r)  # 半径差
    # 注意判断顺序：先判相等（切），再判不等（离/含/交）
    if d > s + EPS:
        return "相离 (Apart)"
    if abs(d - s) < EPS:
        return "外切 (Tangential-Outer)"
    if abs(d - diff) < EPS:
        return "内切 (Tangential-Inner)"
    if d < diff - EPS:
        return "内含 (Contained)"
    # 如果以上都不是，且 d 在 diff 和 s 之间
    return "相交 (Intersecting)"
