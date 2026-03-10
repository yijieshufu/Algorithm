import sys
it =iter(sys.stdin.read().split())
n = int(next(it))
k = int (next(it))
for _ in range(k):
    next(it)
for _ in range(n-1):
    u,v =next(it),next(it)
print(k-1)