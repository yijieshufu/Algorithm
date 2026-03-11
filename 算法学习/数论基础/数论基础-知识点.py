import math
def is_prime(n):
    # 1. 基础检查
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False # 剔除偶数
    # 2. 确定搜索范围（只需到根号n）
    limit = int(math.isqrt(n))
    # 3. 只测试奇数作为因数
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True
