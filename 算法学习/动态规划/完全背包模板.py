# 状态数组初始化
f = [0] * (m + 1)
for _ in range(n): # n物品数量
    w = next(it) # 当前物品重量
    v = next(it) # 当前物品价值
    
    # 完全背包核心：容量正序遍历
    # 从 w 开始，保证 j-w 始终合法
    for j in range(w, m + 1): # m背包总容量
        # 竞赛技巧：Python 中 if 判断更新通常比调用 max() 函数更快
        nv = f[j - w] + v
        if nv > f[j]:
            f[j] = nv
print(f[m])
