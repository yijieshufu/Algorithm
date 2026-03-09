import sys
import math
input = sys.stdin.read().split()
it = iter(input)
n = int(next(it))
p = [None] * (n + 1)
for i in range(1, n + 1):
    p[i] = (float(next(it)), float(next(it)))
a, b, c = float(next(it)), float(next(it)), float(next(it))
div = math.sqrt(a * a + b * b)
ans = sum(1 for i in range(1, n + 1) if abs(a * p[i][0] + b * p[i][1] + c) / div < 1e-3)
print(ans)
