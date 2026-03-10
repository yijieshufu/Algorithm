import sys, bisect

# 增加递归深度
sys.setrecursionlimit(20000)

# 快速输入
it = iter(sys.stdin.read().split())
n, q = int(next(it)), int(next(it))
a = [int(next(it)) for _ in range(n)]

# 建图
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = int(next(it)), int(next(it))
    g[u].append(v); g[v].append(u)

# DFS 序
tin, tout = [0]*n, [0]*n
timer = -1
def dfs(u, p):
    global timer
    timer += 1
    tin[u] = timer
    for v in g[u]:
        if v != p: dfs(v, u)
    tout[u] = timer
dfs(0, -1)

# 分块初始化 把“树上的果实”变成了“排好队的果实”
pos = [[] for _ in range(n)]
for i in range(n): pos[tin[i]].append(a[i])

# 分块算法
sz = 120 # 块大小  题目中 $N = 10,000$，理论值应该是 $\sqrt{10,000} = 100$。
bn = (n + sz - 1) // sz # 块
b = [[] for _ in range(bn)] # 块 的容器
# 把排好队的果实（pos 里的数据）按位置扔进对应的纸箱里 
#extend 是把列表里的果实一个个取出来放进大纸箱 b
for i in range(n): b[i//sz].extend(pos[i])  
for i in range(bn): b[i].sort() # 让每个纸箱里的果实按大小排好序

# 处理操作
ans = []
for _ in range(q):
    u, s = int(next(it)), int(next(it))
    l, r = tin[u], tout[u]
    bl, br = l // sz, r // sz
    cnt = 0
    
    if bl == br: # 同块 
        for i in range(l, r + 1):
            for x in pos[i]:
                if x < s: cnt += 1
    else:#  区间横跨了多个块
        for i in range(l, (bl + 1) * sz):# 左散块
            for x in pos[i]:
                if x < s: cnt += 1
        for i in range(br * sz, r + 1): # 右散块
            for x in pos[i]:
                if x < s: cnt += 1
        for i in range(bl + 1, br): #  中间整块
            cnt += bisect.bisect_left(b[i], s)
            
    ans.append(str(cnt))
    # 更新：新增果实并维护块有序
    pos[tin[u]].append(s)
    bisect.insort(b[tin[u]//sz], s)

sys.stdout.write('\n'.join(ans) + '\n')