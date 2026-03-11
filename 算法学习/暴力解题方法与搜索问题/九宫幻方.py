import os
import sys

# 请在此输入您的代码
data = []
for i in range(3):
    data.append(list(map(int,input().split())))
data1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]] 
data2 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
data3 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]] 
data4 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
data5 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
data6 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
data7 = [[6, 1, 8] ,[7, 5, 3] ,[2, 9, 4]]
data8 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
ans = 0
for t in [data1, data2, data3, data4, data5, data6, data7, data8]:
    ok = 1
    for i in range(3):
        for j in range(3):
            if data[i][j] != 0 and data[i][j] != t[i][j]:
                ok = 0
    if ok:
        output = t
        ans += 1
if ans >= 2:
    print("Too Many")
else:
    for i in output:
        print(*i)
