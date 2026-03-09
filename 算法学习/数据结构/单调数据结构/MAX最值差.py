import sys
from collections import deque

input = sys.stdin.read().split()
it = iter(input)

n = int(next(it))
k = int(next(it))
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(next(it))

q_max = deque()
q_min = deque()
max_diff = 0

for i in range(1, n + 1):
    while q_max and a[q_max[-1]] <= a[i]:
        q_max.pop()
    q_max.append(i)
    if q_max[0] < i - k:
        q_max.popleft()

    while q_min and a[q_min[-1]] >= a[i]:
        q_min.pop()
    q_min.append(i)
    if q_min[0] < i - k:
        q_min.popleft()

    d = a[q_max[0]] - a[q_min[0]]
    if d > max_diff:
        max_diff = d

sys.stdout.write(str(max_diff) + '\n')