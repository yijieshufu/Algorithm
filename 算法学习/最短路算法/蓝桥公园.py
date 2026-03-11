import sys
# 读入数据
it =iter(sys.stdin.read().split())
n = int(next(it)) # n
m = int(next(it)) # m条边
q = int(next(it)) # q查询
# 初始化邻接矩阵 构建图
inf = float("inf")
f = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    f[i][i]=0
# 存入边
for _ in range(m):
    u,v,w = int(next(it)),int(next(it)),int(next(it))
    if w < f[u][v]: 
        f[u][v]=f[v][u]=w
# Floyd 算法
for k in range(1,n+1):
    fk = f[k]
    for i in range(1,n+1):
        fi = f[i]
        if fi[k]==inf :continue
        fik = fi[k]
        for j in range(1,n+1):
            if fik+fk[j]<fi[j]:
                fi[j]=fik+fk[j]
# 查询
for _ in range(q):
    st , ed = int(next(it)),int(next(it))
    ans = f[st][ed]
    print(ans if ans!= inf else -1)