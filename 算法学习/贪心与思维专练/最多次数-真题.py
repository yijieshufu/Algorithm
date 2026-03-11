import os
import sys
it = iter(sys.stdin.read().split())
s = next(it)
l = len(s)
ans = 0
i = 0
target={'l','q','b'}
while i <=l-3:
  sub = s[i:i+3]
  if set(sub) == target:
    ans+=1
    i+=3
  else:i+=1
print(ans)
