import os
import sys

it = iter(sys.stdin.read().split())

n = int(next(it))
a = [int(next(it)) for _ in range(n)]
b = [int(next(it)) for _ in range(n)]
c = [int(next(it)) for _ in range(n)]
p0,p1,p2=0,0,0
m = int(next(it))
ans = 0
for _ in range(m):
  p0 = (p0+int(next(it)))%n
  p1 = (p1+int(next(it)))%n
  p2 = (p2+int(next(it)))%n
  score = 0
  if a[p0]==b[p1]==c[p2]:
    score = max(score,200)
  if a[p0]==b[p1] or a[p0]==c[p2] or b[p1]==c[p2]:
    score = max(score,100)
  if a[p0]+1==b[p1] and b[p1]+1 ==c[p2]:
    score = max(score,200)
  s = sorted([a[p0],b[p1],c[p2]]) 
  if s[0]+1==s[1] and s[1]+1==s[2]:
    score = max(score,100)
  ans +=score
print(ans)
