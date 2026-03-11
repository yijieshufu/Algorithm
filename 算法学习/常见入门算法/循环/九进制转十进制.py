def dec_to_n(x, n):
    t = []
    if x == 0: t.append(0)
    while x > 0:
        t.append(x % n) # 取余数
        x //= n         # 整除
    t.reverse()         # 必须翻转，让高位在前
    
    # 适配你的 1-indexed 要求
    m = len(t)
    a = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i] = t[i-1]
    return a, m # 返回 1 索引数组和它的长度
