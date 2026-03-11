import os
import sys
it = iter(sys.stdin.read().split())
h = int(next(it))
w = int(next(it))
s="2025"
L=4
for i in range(h):# i相当于左移了
  row = []
  for j in range(w):
    row.append(s[(i+j)%L]) 
  print("".join(row))# 每行打印
