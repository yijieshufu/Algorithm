import sys

# 数据读入
it = iter(sys.stdin.read().split())

n = int(next(it))
k = int(next(it))
a = [int(next(it)) for _ in range(n)]

# check h函数
def check(mid):
    for i in range