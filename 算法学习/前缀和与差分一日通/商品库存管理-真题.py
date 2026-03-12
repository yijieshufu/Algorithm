import sys
# 块 1：高效输入流处理
it = iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
ops = []
diff = [0] * (n + 2)
# 记录操作并维护差分
for _ in range(m):
    l, r = int(next(it)), int(next(it))
    ops.append((l, r))
    diff[l] += 1
    diff[r + 1] -= 1
# 块 2：还原库存并统计基础 0
count = [0] * (n + 1) 
base_zeros = 0
curr = 0
for i in range(1, n + 1):
    curr += diff[i]
    count[i] = curr  # 在执行完所有 $m$ 个操作后，第 $i$ 种商品真实的库存总量
    if curr == 0: # 题目初始为0  只加0 统计原本为0 执不执行操作都为0 
        base_zeros += 1
# 块 3：预处理库存为 1 的前缀和
# 一个商品的 count[i] == 1，说明它只被唯一一个操作覆盖了
pre1 = [0] * (n + 1)
for i in range(1, n + 1): 
    pre1[i] = pre1[i - 1] + (1 if count[i] == 1 else 0)
# 块 4：计算每个操作被跳过的结果
ans = []
for l, r in ops:
    # 结果 = 原始 0 数量 + 该区间内库存为 1 的商品数量
    res = base_zeros + (pre1[r] - pre1[l - 1])
    ans.append(str(res))
sys.stdout.write('\n'.join(ans) + '\n')