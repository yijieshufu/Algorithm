import sys

it = iter(sys.stdin.read().split())
X = int(next(it))
# 计算 0 到 n 数字 拼接后 的 总长度
def get_len(n):
    if n < 0: return 0
    res = 1 # 数字 0 占 1 位
    if n == 0: return res
    l, r, bit = 1, 1, 1  # l,r位数的起点  bit这层数有多少位
    while r <= n:
        res += (r - l + 1) * bit  # 个数 * 每个数的位数 = 长度
        bit += 1 #进行下一层的数
        l = r + 1 # 下一层的起点是上一层的终点+1
        r = (l << 1) - 1 # 下一层的终点 是 起点左移1位再-1
    if l <= n:
        res += (n - l + 1) * bit  # 剩下的长度
    return res
# 计算 0 到 n 中所有二进制位 1 的个数 (经典 $O(\log n)$ 算法)
def get_ones(n):
    if n <= 0: return 0
    res = 0
    # 统计每一位上 1 出现的频率
    for i in range(62): # x<10**18  二进制大概是60位 开62位
        cycle = 1 << (i + 1)  # 第i位的二进制的周期变化
        res += (n + 1) // cycle * (cycle // 2) # 整周期里面的1
        res += max(0, (n + 1) % cycle - (cycle // 2)) # 剩余周期里面的1
    return res

# 1. 二分查找：找到第 X 位所在的那个数字 N
low, high = 0, X
N = high  # N 要确定的 假设最大为X 很安全 要找的数 肯定是小于X的
while low <= high:
    mid = (low + high) // 2
    if get_len(mid) >= X: # get_len() 获取的是总的长度 也就是拼接的二进制
        N = mid #找到那个数了
        high = mid - 1 # 范围大了
    else:
        low = mid + 1 # 范围小了

ans = get_ones(N - 1) # 0到N-1之前的1
rem = X - get_len(N - 1) # 剩下N这个数的 二进制的数
# 将 N 转为二进制字符串（去掉 '0b'）
s_n = bin(N)[2:]
# 如果是数字 0，特殊处理
for i in range(rem):
    if s_n[i] == '1':
        ans += 1
print(ans)