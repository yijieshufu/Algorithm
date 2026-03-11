import os
import sys
limit=100000
is_prime=[True]*(limit+1)
is_prime[1]=False
prime=[]
target=2025
for i in range(2,limit+1):
  if is_prime[i]:
    prime.append(i)
    if len(prime) == target:
      print(prime[-1])
    for j in range(i*i,limit+1,i):
      is_prime[j]=False
