import sys
# 1. 棋盘初始化：-1 表示空。根据图片提取的固定点索引：值
g = [-1] * 36
for i, v in [(0, 1), (1, 0), (3, 0), (9, 0), (16, 0), (17, 0), (26, 1), (29, 1), (31, 0), (34, 1)]:
    g[i] = v
def dfs(idx):
    if idx == 36:
        # 校验行、列唯一性：将列表切片成 6 行，zip(*) 转置成 6 列
        rows = [tuple(g[i:i + 6]) for i in range(0, 36, 6)] # 转变成元组类型 6行 每行变成了元组 后面才能使用set去重
        cols = list(zip(*rows)) # zip 每行取第一个
        if len(set(rows)) == 6 and len(set(cols)) == 6: # set去重机制使得每行每列的排列方式一样 要达到六个
            print("".join(map(str, g)))# 取出g中的每个元素 为str类型 打印输出
            return True
        return False
    if g[idx] != -1: return dfs(idx + 1)
    r, c = divmod(idx, 6) # (idx // 6, idx % 6) divmod 函数得到r,c
    for v in (0, 1): # 填入 0白棋，1黑棋
        g[idx] = v
        row = g[r * 6: r * 6 + 6] # 取这行的元素
        col = [g[i * 6 + c] for i in range(6)] # 取这列的元素
        # 核心剪枝：1. 事不过三(行列)；2. 行/列内 v 的总数不过 3
        row_limit = (c < 2 or not (v == g[idx - 1] == g[idx - 2])) and row.count(v) <= 3
        col_limit = (r < 2 or not (v == g[idx - 6] == g[idx - 12])) and col.count(v) <= 3
        if row_limit and col_limit:
            if dfs(idx + 1): return True # 汇报工作
    g[idx] = -1  # 回溯 擦掉
    return False
dfs(0)

