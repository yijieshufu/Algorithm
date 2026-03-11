import sys
# 数据读入
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
# 并查集
p = list(range(n + 1))
cnt = n # 连通块计数
ans = 0
# 路径压缩
def find(x):
    if x!= p[x]:
        p[x]= find(p[x])
    return p[x]
# 录入边
edges = []
for _ in range(m):
    u,v,w = int(next(it)),int(next(it)),int(next(it))
    edges.append((u,v,w))
edges.sort(key= lambda x:x[2])
for u,v,w in edges:
    root_u = find(u);root_v = find(v)
    if root_u!= root_v:
        p[root_u] = root_v
        ans = w 
        cnt -=1
        if cnt ==1 :break
print(ans if cnt ==1 else -1)