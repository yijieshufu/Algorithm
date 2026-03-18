import sys

# 1.变量
it = iter(sys.stdin.read().split())
m = int(next(it))  # 组数 T
# 3.操作
for _ in range(m):
    n = int(next(it))  # 每组的人数 n
    ans = 0  # 每一组的答案必须重置

    # 用 f 代表第 0 人的状态，g 代表第 1 人的状态
    for f in range(2):
        for g in range(2):
            # a: 存储身份序列，多开两位用于最后“接水管”比对
            a = [0] * (n + 2)
            a[0], a[1] = f, g

            # b: 作为填充序列的指针
            for b in range(n):
                a[b + 2] = a[b] ^ a[b + 1]

            # 闭环检查：算出来的“虚像” a[n], a[n+1] 必须等于“本体” a[0], a[1]
            if a[n] == a[0] and a[n + 1] == a[1]:
                # 只有逻辑通了，才开始统计这组里的说谎者(0)
                for b in range(n):
                    if a[b] == 0:
                        ans += 1

    # 4.答案
    print(ans)