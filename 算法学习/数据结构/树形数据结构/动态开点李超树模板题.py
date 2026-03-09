import sys
it = iter(sys.stdin.read().split())

def build_convex_hull(lines):
    hull = []
    for k, b in lines:
        while len(hull) >= 2:
            k1, b1, k2, b2 = hull[-2][0], hull[-2][1], hull[-1][0], hull[-1][1]
            if (b1 - b2) * (k - k2) >= (b2 - b) * (k2 - k1):
                hull.pop()
            else:
                break
        hull.append((k, b))
    return hull

def query_max(hull, x):
    l, r = 0, len(hull) - 1
    while l < r:
        mid = (l + r) // 2
        v1, v2 = hull[mid][0] * x + hull[mid][1], hull[mid + 1][0] * x + hull[mid + 1][1]
        l, r = (mid + 1, r) if v1 <= v2 else (l, mid)
    return hull[l][0] * x + hull[l][1]

N, M = int(next(it)), int(next(it))
B = [0] + [int(next(it)) for _ in range(N)]
B[1:] = sorted(B[1:])
C = [0] + [int(next(it)) for _ in range(M)]
lines = [(N - i + 1, B[i] * (N - i + 1)) for i in range(N, 0, -1)]
hull = build_convex_hull(lines)
print(" ".join(str(query_max(hull, C[j])) for j in range(1, M + 1)))
