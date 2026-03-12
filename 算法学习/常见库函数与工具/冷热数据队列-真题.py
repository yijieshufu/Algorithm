import sys
from collections import OrderedDict

# 输入流快速读取
it = iter(sys.stdin.read().split())
n1 = int(next(it))
n2 = int(next(it))
m = int(next(it))
q1 = OrderedDict()
q2 = OrderedDict()
for _ in range(m):
    p = next(it)
    if p in q1: # 已经在 q1，只需移到 q1 首部 [块 2]
        q1.move_to_end(p, last=False)
    elif p in q2: # 在 q2，提升到 q1 首部 [块 2]
        del q2[p]
        q1[p] = True # 无意义的占号
        q1.move_to_end(p, last=False)
        # 此时 q1 长度可能 +1，需检查溢出 [块 3]
        if len(q1) > n1:
            out_p, _ = q1.popitem(last=True)
            if len(q2) < n2: # Rule 4: q2 未满才接收
                q2[out_p] = True
                q2.move_to_end(out_p, last=False)
    else: # 全都不在，插入 q2 首部 [块 1]
        q2[p] = True
        q2.move_to_end(p, last=False)
        # 检查 q2 是否溢出 [块 1]
        if len(q2) > n2:
            q2.popitem(last=True)
# 格式化输出
print(*(q1.keys()))
print(*(q2.keys()))