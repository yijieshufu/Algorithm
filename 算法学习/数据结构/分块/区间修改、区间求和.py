import sys
input = sys.stdin.read().split()
it = iter(input)

n, q = int(next(it)), int(next(it))
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(next(it))

tree = [0] * (4 * n + 1)
tag = [0] * (4 * n + 1)

def push_up(u):
    tree[u] = tree[u << 1] + tree[u << 1 | 1]

# 懒标记下传：把当前节点加的 k 分摊给左右子区间
def push_down(u, l, r):
    if tag[u]:
        mid = (l + r) // 2
        tag[u << 1] += tag[u]
        tree[u << 1] += tag[u] * (mid - l + 1)
        tag[u << 1 | 1] += tag[u]
        tree[u << 1 | 1] += tag[u] * (r - mid)
        tag[u] = 0

def build(u, l, r):
    if l == r:
        tree[u] = a[l]
        return
    mid = (l + r) // 2
    build(u << 1, l, mid)
    build(u << 1 | 1, mid + 1, r)
    push_up(u)

# 区间 [L,R] 加 k：被完全覆盖则打标记，否则下传后递归
def update(u, l, r, L, R, k):
    if L <= l and r <= R:
        tree[u] += k * (r - l + 1)
        tag[u] += k
        return
    push_down(u, l, r)
    mid = (l + r) // 2
    if L <= mid:
        update(u << 1, l, mid, L, R, k)
    if R > mid:
        update(u << 1 | 1, mid + 1, r, L, R, k)
    push_up(u)

# 区间 [L,R] 求和：被完全覆盖直接返回，否则下传后递归左右
def query(u, l, r, L, R):
    if L <= l and r <= R:
        return tree[u]
    push_down(u, l, r)
    mid = (l + r) // 2
    res = 0
    if L <= mid:
        res += query(u << 1, l, mid, L, R)
    if R > mid:
        res += query(u << 1 | 1, mid + 1, r, L, R)
    return res

build(1, 1, n)
for _ in range(q):
    op = next(it)
    if op == '1':
        l, r, k = int(next(it)), int(next(it)), int(next(it))
        update(1, 1, n, l, r, k)
    else:
        l, r = int(next(it)), int(next(it))
        print(query(1, 1, n, l, r))
