import os
import sys
it = iter(sys.stdin.read().split())
n=int(next(it))
MOD=1000000007
if n==1:
  print(1)
else:
  print(2*pow(3,n-2,MOD)%MOD)
