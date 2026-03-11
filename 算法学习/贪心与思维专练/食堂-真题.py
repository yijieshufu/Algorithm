import sys

# 增加递归深度，防止爆栈 (蓝桥杯基石操作)
sys.setrecursionlimit(5000)
# 全局备忘录：跨越 100 组查询共享状态，究极加速！
memo = {}
def solve(a2, a3, a4, b4, b6):
    # 终点站：如果所有学生都安排完了，或者桌子用光了，能增加的人数就是 0
    if (a2 == 0 and a3 == 0 and a4 == 0) or (b4 == 0 and b6 == 0):
        return 0
    state = (a2, a3, a4, b4, b6)
    if state in memo:
        return memo[state]
    ans = 0
    # 第一阶段：优先疯狂压榨 6 人桌
    if b6 > 0:
        if a4 >= 1:
            if a2 >= 1: ans = max(ans, 6 + solve(a2 - 1, a3, a4 - 1, b4, b6 - 1)) # 完美 4+2
            else: ans = max(ans, 4 + solve(a2, a3, a4 - 1, b4, b6 - 1))           # 只能坐 4
        if a3 >= 2:
            ans = max(ans, 6 + solve(a2, a3 - 2, a4, b4, b6 - 1))                 # 完美 3+3
        if a3 >= 1:
            if a2 >= 1: ans = max(ans, 5 + solve(a2 - 1, a3 - 1, a4, b4, b6 - 1)) # 凑合 3+2
            else: ans = max(ans, 3 + solve(a2, a3 - 1, a4, b4, b6 - 1))           # 只能坐 3
        if a2 >= 3:
            ans = max(ans, 6 + solve(a2 - 3, a3, a4, b4, b6 - 1))                 # 完美 2+2+2
        elif a2 == 2:
            ans = max(ans, 4 + solve(0, a3, a4, b4, b6 - 1))                      # 凑合 2+2
        elif a2 == 1:
            ans = max(ans, 2 + solve(0, a3, a4, b4, b6 - 1))                      # 只能坐 2
            
    # 第二阶段：6 人桌用完后，榨干 4 人桌
    else:
        if a4 >= 1:
            ans = max(ans, 4 + solve(a2, a3, a4 - 1, b4 - 1, 0))                  # 完美 4
        if a3 >= 1:
            ans = max(ans, 3 + solve(a2, a3 - 1, a4, b4 - 1, 0))                  # 凑合 3
        if a2 >= 2:
            ans = max(ans, 4 + solve(a2 - 2, a3, a4, b4 - 1, 0))                  # 完美 2+2
        elif a2 == 1:
            ans = max(ans, 2 + solve(a2 - 1, a3, a4, b4 - 1, 0))                  # 只能坐 2
            
    memo[state] = ans
    return ans

# --- 极简 I/O 起手式 ---

it = iter(sys.stdin.read().split())
q = int(next(it))
for _ in range(q):
    a2 = int(next(it))
    a3 = int(next(it))
    a4 = int(next(it))
    b4 = int(next(it))
    b6 = int(next(it))
    print(solve(a2, a3, a4, b4, b6))
