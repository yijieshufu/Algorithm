import os
import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
t = int(next(it))
MAX_N = 15 + 1 # 题目 n 最大 15 
c = [[0] * MAX_N for _ in range(MAX_N)]
for i in range(MAX_N):
        c[i][0] = 1 # 任何数选 0 个，都只有 1 种取法（空取）
        for j in range(1, i + 1):
            c[i][j] = c[i-1][j] + c[i-1][j-1]
for _ in range(t):
  n = int(next(it))
  m = int(next(it))
  print(c[n][m])
