import sys
with open("log.txt", "r") as f:
    it = iter(f.read().split())
ans = 0
cur = 0
pre_t = -2000
while True:
    try:
        target = next(it)
        user = next(it)
        t = int(next(it))
        if target == user:
            if cur == 0 or t - pre_t <= 1000:
                cur +=1
            else:
                ans = max(ans, cur)
                cur = 1
            pre_t = t
        else:
            ans = max(ans, cur)
            cur = 0
    except StopIteration:
        # 迭代器耗尽，跳出循环
        break
ans = max(ans, cur)
print(ans)
