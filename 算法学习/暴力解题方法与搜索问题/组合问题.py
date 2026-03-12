import sys

# 输入流初始化
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))

res = [] # [块 1: 路径记录]

def dfs(u, start):
    if u == m: # [块 3: 边界到达]
        print(*(res))
        return
    
    # 剪枝优化：如果后面剩下的数不够凑齐 m 个，就没必要选了
    for i in range(start, n + 1): # [块 2: 核心选择逻辑]
        if n - i + 1 < m - u: break 
        res.append(i)
        dfs(u + 1, i + 1) # 传 i+1 保证不重复选且有序
        res.pop()

dfs(0, 1)