import sys
import collections from deque

# 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it))
# 边界
if n ==1:
    print(0)
    sys.exit()
# 创建邻接表
g = [[] for _ in range(n+1)]
total_w = 0
for _ in range(n-1):
    v,u,w=int(next(it)),int(next(it)),int(next(it))
    g[u].append(v);g[v].append(u)
    total_w+=w 
# DFS 深度搜索 求树的直径
def get_farthest(state):
    