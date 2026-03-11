import os
import sys
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a
ans=0
for i in range(1,2021):
  for j in range(1,2021):
    if gcd(i,j) == 1:
      ans+=1
print(ans)
