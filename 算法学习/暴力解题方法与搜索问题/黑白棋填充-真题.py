import os
import sys

# 初始化 棋盘 都为 -1  1黑 0 白
g=[-1]*36
# 读入棋盘 [(0, 1), (1, 0), (3, 0), (9, 0), (16, 0), (17, 0), (26, 1), (29, 1), (31, 0), (34, 1)]
for idx,v in [(0, 1), (1, 0), (3, 0), (9, 0), (16, 0), (17, 0), (26, 1), (29, 1), (31, 0), (34, 1)]:
  g[idx]=v
# 使用dfs 每个点进行判断
def dfs(idx):
  # 第一步 先判断是否到达终点
  if idx == 36:
    # 达到终点 36
    # 预处理 拿到每行每列 行：使用tuple后才能set 列：zip()作用 是每行那一个元素
    rows =[tuple(g[i:i+6]) for i in range(0,36,6)]
    cols =list(zip(*rows))
    # 判断 每行每列的排列方式是否一样 ：set去重机制
    if len(set(rows))==6 and len(set(cols))==6:
      print("".join(map(str,g)))
      return True
    return False
  # 第二步：判断当前位置 是否有棋子，有则下一个位置
  if g[idx]!=-1: return dfs(idx+1)
  # 第三步：填入具体的棋子
  for v in (0,1):
    # 得到当前的行列坐标 使用divmod
    g[idx]=v
    r,c=divmod(idx,6)
    # 取行列的所有元素
    row = g[r*6:r*6+6]
    col = [g[i*6+c] for i in range(6)]
    # 验证 题目的不能同时出现  “黑黑黑” 或 “白白白”  和 黑色棋子和白色棋子的数量必须相等 ==> 黑白都不能超过3
    row_limit= (c<2 or not v==g[idx-1]==g[idx-2]) and row.count(v)<=3
    col_limit= (r<2 or not v==g[idx-6]==g[idx-12]) and col.count(v)<=3
    # 成功 进行下一个元素
    if row_limit and col_limit:
      if dfs(idx+1):return True
    # 失败 回溯 擦掉 当前位置
  g[idx]=-1
  return False
dfs(0)
