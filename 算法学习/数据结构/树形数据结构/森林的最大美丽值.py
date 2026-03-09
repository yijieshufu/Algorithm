import sys
input = sys.stdin.read().split()
it = iter(input)

def binary_search(l, r, check_func):
    ans = l
    while l <= r:
        mid = (l + r) // 2
        if check_func(mid):
            ans, l = mid, mid + 1
        else:
            r = mid - 1
    return ans

n, m, k = int(next(it)), int(next(it)), int(next(it))
h = [0] + [int(next(it)) for _ in range(n)]

def check(mid):
    diff = [0] * (n + 2)
    total_days = cur_add = 0
    for i in range(1, n + 1):
        cur_add += diff[i]
        if h[i] + cur_add < mid:
            need = mid - (h[i] + cur_add)
            total_days += need
            if total_days > m:
                return False
            cur_add += need
            if i + k <= n:
                diff[i + k] -= need
    return True

low, high = min(h[1:]), max(h[1:]) + m
print(binary_search(low, high, check))
