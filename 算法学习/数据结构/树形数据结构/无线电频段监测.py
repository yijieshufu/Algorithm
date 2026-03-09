import sys
input = sys.stdin.read().split()
it = iter(input)
q = int(next(it))
ops = [(int(next(it)), int(next(it)), int(next(it)), int(next(it))) for _ in range(q)]
pts = set()
for t, l, r, _ in ops:
    pts.add(l)
    pts.add(r + 1)
p = sorted(pts)
m = len(p)
v_arr = [0] * (m + 1)
l_arr = [0] * (m + 1)
for i in range(1, m):
    l_arr[i] = p[i] - p[i - 1]
for t, ql, qr, qv in ops:
    if t == 1:
        for j in range(1, m):
            if p[j - 1] >= ql and p[j] - 1 <= qr:
                v_arr[j] += qv
    else:
        ans = sum(l_arr[j] for j in range(1, m) if p[j - 1] >= ql and p[j] - 1 <= qr and v_arr[j] >= qv)
        print(ans)
