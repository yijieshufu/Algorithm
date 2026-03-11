import sys
it = iter(sys.stdin.read().split())
n = int(next(it))
nums=[next(it) for _ in range(n)]
M = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
res= []
for s in nums:
  sum =0
  for char in s:
    sum+=M[int(char)]
  items=(sum,int(s),s)
  res.append(items)
res.sort()
ans = []
for results in res:
  ans.append(results[2])
print(*ans)
