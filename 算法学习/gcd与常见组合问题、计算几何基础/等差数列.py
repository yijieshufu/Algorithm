import os
import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(x) for x in it]
a.sort()
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a
d = 0
for i in range(1,n):
  diff = a[i]-a[i-1]
  if diff == 0:
    d = diff
  else:
    d = gcd(d,diff)
min_a = a[0]
max_a = a[-1]
if d == 0:print(n)
else:
  ans = (max_a-min_a)//d +1
  print(ans)
