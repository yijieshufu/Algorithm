import sys
# 块 3：输入流初始化
it = iter(sys.stdin.read().split())
n = int(next(it))
# 块 1：定义状态容器
d = {}
for _ in range(n):
    op = next(it)
    if op == 'add':
        # 块 2：核心更新（忽略无用的 bookname）
        _book = next(it)
        au = next(it)
        d[au] = d.get(au, 0) + 1
    else:
        # 块 2：核心查询
        au = next(it)
        print(d.get(au, 0))