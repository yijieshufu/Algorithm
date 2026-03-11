import os
import sys
it = iter(sys.stdin.read().split())
T = int(next(it))
for _ in range(T):
  # 读取 A, B, C 三个点的坐标
  xa, ya = float(next(it)), float(next(it))
  xb, yb = float(next(it)), float(next(it))
  xc, yc = float(next(it)), float(next(it))
  # 1. 计算向量 AB (x1, y1) 和 向量 AC (x2, y2)
  x1, y1 = xb - xa, yb - ya
  x2, y2 = xc - xa, yc - ya
  # 2. 计算叉积的绝对值 (即平行四边形的面积)
  # 叉积公式: x1*y2 - x2*y1
  area = 0.5*abs(x1 * y2 - x2 * y1)
  print("{:.2f}".format(area))
