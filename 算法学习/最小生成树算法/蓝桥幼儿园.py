import sys
sys.setrecursionlimit(300000)
it = iter(sys.stdin.read().split())
n,m= int(next(it)),int(next(it))
# 并查集
p =list(range(n+1))
def find(x):
    if x!=p[x]:
        p[x] = find(p[x])
    return p[x]
for _ in range(m):
    op = next(it)
    x = int(next(it))
    y = int(next(it))
    root_x,root_y=find(x),find(y)
    if op =='1':
        if root_x!=root_y:p[root_x]=root_y
    else:
      if root_x==root_y:
        sys.stdout.write("YES\n")
      else:
        sys.stdout.write("NO\n")