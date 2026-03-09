import sys
input = sys.stdin.read().split()
it = iter(input)

n = int(next(it))
tree = [0] * (n + 1)

def update(x, val):
    while x <= n:
        tree[x] += val
        x += x & -x

def query(x):
    r = 0
    while x > 0:
        r += tree[x]
        x -= x & -x
    return r

for i in range(1, n + 1):
    update(i, int(next(it)))

m = int(next(it))
for _ in range(m):
    op = int(next(it))
    if op == 1:
        update(int(next(it)), int(next(it)))
    else:
        a, b = int(next(it)), int(next(it))
        sys.stdout.write(str(query(b) - query(a - 1)) + '\n')
