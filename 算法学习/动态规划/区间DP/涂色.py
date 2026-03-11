import sys

it = iter(sys.stdin.read().split())
s = next(it, '')
n = len(s)
if not s:
    print(0)
    exit()

s = ' ' + s                          # 1-based
f = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    f[i][i] = 1

for l in range(2, n + 1):            # 枚举长度
    for i in range(1, n - l + 2):    # 枚举左端点
        j = i + l - 1
        if s[i] == s[j]:
            f[i][j] = min(f[i + 1][j], f[i][j - 1])
        else:
            f[i][j] = min(f[i][k] + f[k + 1][j] for k in range(i, j))

print(f[1][n])
