import sys
from collections import deque
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
    g[u].append((v,w));g[v].append((u,w))
    total_w+=w 
# DFS 深度搜索 求树的直径
def get_farthest(state):
    dist = [-1]*(n+1)
    dist[state] = 0
    q = deque([state])
    target,max_d = state,0

    while q:
        u = q.popleft()
        if dist[u] > max_d:
            max_d,target = dist[u],u
        for v,w in g[u]:
            if dist[v] ==-1:
                dist[v] = dist[u]+w
                q.append(v)
    return target,max_d

# 两次DFS
p,_ =get_farthest(1)
_,diameter = get_farthest(p)
print(2*total_w-diameter)

         