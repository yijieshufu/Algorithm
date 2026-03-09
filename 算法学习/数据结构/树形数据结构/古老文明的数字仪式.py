import sys, heapq
it = iter(sys.stdin.read().split())
n, m = int(next(it)), int(next(it))
a = [0] + [int(next(it)) for _ in range(n)]
qs = sorted((int(next(it)), i) for i in range(1, m+1))
ans, L, R, idx = [0] * (m + 1), [], [], 0

def add(x):
    if not L or x <= -L[0]:
        heapq.heappush(L, -x)
    else:
        heapq.heappush(R, x)
    while len(L) > len(R) + 1:
        heapq.heappush(R, -heapq.heappop(L))
    while len(R) > len(L):
        heapq.heappush(L, -heapq.heappop(R))

for k, i in qs:
    while idx < k: idx += 1; add(a[idx])
    ans[i] = -L[0]
print('\n'.join(str(ans[i]) for i in range(1, m+1)))
