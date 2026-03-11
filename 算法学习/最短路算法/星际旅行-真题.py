import sys
# 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
q = int(next(it))
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = int(next(it)), int(next(it))
    g[u].append(v)
    g[v].append(u)
# 全源 BFS 与前缀和预处理
f = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dist =[-1]*(n+1)
    dist[i] = 0
    que = [i]
    # DBS 算的是 当前节点到该节点的距离
    for u in que:
        for v in g[u]:
            if dist[v]==-1:
                dist[v]=dist[u]+1
                que.append(v)
    # i 走d步 的 有多少能到达的星球数量 
    for d in dist:
        if d != -1:
            f[i][d]+=1
    # 前缀和 计算 小于等于d的星球
    for d in range(1,n+1):
        f[i][d]+=f[i][d-1]
# 查询 计算期望
ans=0
for _ in range(q):
    x,y = int(next(it)),int(next(it))
    ans+=f[x][min(n,y)]
print(f"{ans/q:.2f}")