import os
import sys
from functools import cmp_to_key
it = iter(sys.stdin.read().split())
n = int(next(it))
bins=[bin(i)[2:] for i in range(1,n+1)]
def compare(a,b): 
  if a+b>b+a:
    return -1 # a在b的前面
  return 1
bins.sort(key=cmp_to_key(compare))
print(int("".join(bins),2))
