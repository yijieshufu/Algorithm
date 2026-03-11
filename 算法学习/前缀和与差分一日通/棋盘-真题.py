import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
diff = [[0]*(n+2) for _ in range(n+2)]
for _ in range(m):
  x1 = int(next(it))
  y1 = int(next(it))
  x2 = int(next(it))
  y2 = int(next(it))
  diff[x1][y1]+=1
  diff[x1][y2+1]-=1
  diff[x2+1][y1]-=1
  diff[x2+1][y2+1]+=1  # 先记录好
for i in range(1,n+1):
  row_res = []
  for j in range(1,n+1):
    # 通过二维前最后求值
    diff[i][j]+=diff[i-1][j]+diff[i][j-1]-diff[i-1][j-1] 
    if diff[i][j]%2==1:
      row_res.append('1')
    else:
      row_res.append('0')
  sys.stdout.write("".join(row_res) + "\n")
