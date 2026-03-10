import sys

it = iter(sys.stdin.read().split())

n =int(next(it))
ans_max=0
ans_min=inf
for _ in range(n):
    a = int(next(it))
    b = int(next(it))
    v_max = a//b
    v_min = a//(b+1) +1
    ans_max=max(v_max,ans_max)
    ans_min=min(v_min,ans_min)

print(ans_min,end=" ")
print(ans_max)
