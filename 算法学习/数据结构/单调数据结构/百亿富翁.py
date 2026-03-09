import sys
input = sys.stdin.read().split()
it = iter(input)

n = int(next(it))
h = [0] * (n + 1)
L = [-1] * (n + 1)
R = [-1] * (n + 1)
for i in range(1, n + 1):
    h[i] = int(next(it))

stack = []
for i in range(1, n + 1):
    while stack and h[stack[-1]] <= h[i]:
        stack.pop()
    if stack:
        L[i] = stack[-1]
    stack.append(i)

stack = []
for i in range(n, 0, -1):
    while stack and h[stack[-1]] <= h[i]:
        stack.pop()
    if stack:
        R[i] = stack[-1]
    stack.append(i)

print(*(L[1:]))
print(*(R[1:]))