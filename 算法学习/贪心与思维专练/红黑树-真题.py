import os
import sys
it = iter(sys.stdin.read().split())
m= int(next(it))
for _ in range(m):
  n= int(next(it))
  k= int(next(it))
  p= bin(k-1).count('1')
  if p%2:
    print("BLACK")
  else:
    print("RED")
