import sys

# 设置递归深度，防止处理 18 位数字时溢出
sys.setrecursionlimit(2000)
# [块 1: 核心 I/O 起手式] 
# 使用模板中推荐的极简高效输入
input_data = sys.stdin.read().split()
if not input_data:
    exit()
it = iter(input_data)

n_str = next(it)
a_limit = int(next(it))
b_limit = int(next(it))

nums = [int(c) for c in n_str]
n = len(nums)
memo = {}

def dfs(idx, a, b):
    # [块 3: 边界与初始化]
    if idx == n:
        return 0
    # 检查记忆化
    state = (idx, a, b)
    if state in memo:
        return memo[state]
    d = nums[idx]
    res = 0
    p10 = 10**(n - 1 - idx) # 当前位权重
    # [块 1 & 2: 核心推导 - 决策分支]
    # 方案 1: 尝试用减法 (B) 绕回 9
    if b >= d + 1:
        res = max(res, 9 * p10 + dfs(idx + 1, a, b - (d + 1)))
        
    # 方案 2: 尝试用加法 (A) 增加
    # 贪心：高位即使到不了 9，多加 1 也是赚的
    use_a = min(a, 9 - d)
    res = max(res, (d + use_a) * p10 + dfs(idx + 1, a - use_a, b))
    
    memo[state] = res
    return res

# 顺序执行并输出结果
print(dfs(0, a_limit, b_limit))