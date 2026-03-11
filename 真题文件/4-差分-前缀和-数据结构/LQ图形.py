import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
w=int(next(it))
h=int(next(it))
v=int(next(it))
for _ in range(h):
  print('Q' * w)
for _ in range(w):
  print('Q' * (w + v))
