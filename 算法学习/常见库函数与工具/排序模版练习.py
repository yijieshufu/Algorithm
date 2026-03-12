import sys

# 极简 I/O 起手式
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
# [块 1：遍历未排序序列]
for i in range(1, n):
    v = a[i]
    j = i - 1
    # [块 2：有序区比较与后移]
    while j >= 0 and a[j] > v:
        a[j + 1] = a[j] 
        j -= 1
    # [块 3：插入目标位置]
    a[j + 1] = v
print(*(a))