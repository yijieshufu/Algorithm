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
  area_x2 = abs(x1 * y2 - x2 * y1)
  # 3. 计算底边 AB 的长度 (底)
  base = (x1**2 + y1**2)**0.5
  # 4. 计算距离 (高 = 面积 / 底)
  # 注意：area_x2 已经是 2 倍面积了，直接除以 base 即可
  if base == 0:
      # 如果 A, B 重合，距离就是点 C 到点 A 的距离
      dist = (x2**2 + y2**2)**0.5
  else:
      dist = area_x2 / base
  # 输出结果，保留两位小数
  print("{:.2f}".format(dist))
