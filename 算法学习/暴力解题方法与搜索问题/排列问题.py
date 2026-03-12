import sys

# 输入流初始化
it = iter(sys.stdin.read().split())
n = int(next(it))

# 认知块 1：定义路径与状态位
path = [0] * n
st = [False] * (n + 1)

def dfs(u):
    # 认知块 3：递归终止，输出结果
    if u == n:
        print(*(path))
        return
    # 认知块 2：按 1~n 顺序枚举，确保字典序
    for i in range(1, n + 1):
        if not st[i]:
            path[u] = i
            st[i] = True   # 标记使用
            dfs(u + 1)     # 向下递归
            st[i] = False  # 恢复现场 (回溯关键)

# 执行入口
dfs(0)