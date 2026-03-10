import sys 
sys.setrecursionlimit(10000)
# 读入数据
it = iter(sys.stdin.read().split())
n = int(next(it));m = int(next(it))

# 初始化 父列表 和sz
p = list(range(n+1))
sz = [1]*(n+1) #节点数量

# find(路径压缩)
def find(x):
    if p[x]!=x:
        p[x] = find(p[x])
    return p[x]
# 合并边
for _ in range(m):
    u = int(next(it));v = int(next(it))
    u_root = find(u);v_root = find(v)
    if u_root!=v_root:
        p[u_root]=v_root
        sz[v_root]+=sz[u_root]
# 统计 各个联通的数量 取最小值
ans = n+1
for i in range(1,n+1):
    if p[i]==i:
        ans = min(ans,sz[i])
print(ans)