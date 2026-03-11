import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
s = [0] * (n + 1)
for i in range(n):
  s[i+1]=s[i] ^ a[i] # 异或前缀
ans = 0
for k in range(21):
  cnt0 = 0
  cnt1 = 0
  for i in range(n + 1):
    if (s[i] >> k) & 1:
      cnt1+=1
    else:
      cnt0+=1
  ans += (cnt0 * cnt1) * (1 << k)
print(ans)
