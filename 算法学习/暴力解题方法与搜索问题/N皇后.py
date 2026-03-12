import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
col = [0] * 20   # 块1：列标记
dg = [0] * 40    # 块1：正对角线 r+c
udg = [0] * 40   # 块1：反对角线 r-c+n
ans = 0
def dfs(u):
    global ans
    if u == n:   # 块3：到达边界
        ans += 1
        return
    for i in range(n): # 块2：遍历当前行的每一列
        if not col[i] and not dg[u+i] and not udg[u-i+n]:
            col[i] = dg[u+i] = udg[u-i+n] = 1 # 标记占用
            dfs(u + 1)
            col[i] = dg[u+i] = udg[u-i+n] = 0 # 块3：回溯还原
dfs(0)
print(ans)