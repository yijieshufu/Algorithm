import sys
# 1. 初始化并查集与输入
it = iter(sys.stdin.read().split())
n, m = int(next(it)), int(next(it))
ss = [next(it) for _ in range(n)]
p = list(range(n))
def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]
ans, cnt = 0, 0
# 倒叙L
for L in range(m,0,-1):
    d ={}
    for i in range(n): # 字符串下标
        s2 = ss[i] + ss[i]
        subs = {s2[j:j+L] for j in range(m)}
        for s in subs:
            if s not in d :d[s]=[]
            d[s].append(i)
    for ids in d.values():# d.values 只取里面的值 不要看key
        for i in range(1,len(ids)):
            u,v = find(ids[0]),find(ids[i])
            if u!=v:
                p[u]=v
                ans,cnt = ans+L,cnt+1
    if cnt == n-1: break
print(ans)