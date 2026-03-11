import os
import sys
from collections import OrderedDict
it = iter(sys.stdin.read().split())
n1 = int(next(it))
n2 = int(next(it))
m = int(next(it))
q1=OrderedDict()
q2=OrderedDict()
for _ in range(m):
  p =next(it)
  if p in q1:
    q1.move_to_end(p,last=False)
  elif p in q2:
    del q2[p]
    q1[p] = True 
    q1.move_to_end(p,last=False)
    if len(q1)> n1:
      out_p,_ = q1.popitem(last=True)
      if len(q2)<n2:
        q2[out_p]=True
        q2.move_to_end(out_p,last=False)
  else:
    q2[p] = True
    q2.move_to_end(p,last=False)
    if len(q2)>n2:
      q2.popitem(last=True)
print(*(q1.keys()))
print(*(q2.keys()))
