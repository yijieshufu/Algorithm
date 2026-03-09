import sys

# 使用标准模板起手式，提升读入效率
it = iter(sys.stdin.read().split())
n = int(next(it))  # 阀门数
m = int(next(it))  # 管道长度
a = [(int(next(it)), int(next(it))) for _ in range(n)]  # 存储 (位置, 时间)


def check(t):
    q = []
    for x, s in a:
        if t >= s:
            d = t - s
            # 裁剪区间并存入列表
            q.append((max(1, x - d), min(m, x + d)))

    if not q: return False
    q.sort()  # 按左端点排序是区间合并的前提

    # 必须从第 1 段开始覆盖
    if q[0][0] > 1: return False

    cur = q[0][1]  # 当前覆盖的最右边界
    for i in range(1, len(q)):
        # 核心：离散段接力逻辑
        if q[i][0] <= cur + 1:
            if q[i][1] > cur: cur = q[i][1]
        else:
            break
    return cur >= m


# 二分查找
l, r, ans = 0, 2000000000, 0
while l <= l:  # 此处更正为 l <= r
    mid = (l + r) // 2
    if check(mid):
        ans, r = mid, mid - 1
    else:
        l = mid + 1
print(ans)