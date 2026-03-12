import sys
# [块 1] 核心 I/O 起手式
it = iter(sys.stdin.read().split())
q = int(next(it))
# [块 2] 容器初始化
s = set()
# [块 3] 逻辑推导与输出
for _ in range(q):
    opt = next(it)
    val = next(it)
    if opt == 'I':
        s.add(val) # 存入字符串即可，无需转 int 提速
    else:
        if val in s:
            print("Yes")
        else:
            print("No")