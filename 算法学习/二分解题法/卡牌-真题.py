import sys
# 输入数据
it= iter(sys.stdin.read().split())
n = int(next(it))
m = int(next(it))
a = [int(next(it)) for _ in range(n)]
b = [int(next(it)) for _ in range(n)]
# 二分判断函数
def check(mid):
  # 判断小于套牌mid的
  needed = 0
  for i in range(n):
    if a[i] <mid: 
      need = mid -a[i]
      if need > b[i]:#限制条件 手写牌最多b[i]张
        return False
      needed+=need
      if needed>m:# 限制条件：只有m张空白牌
        return False
  return True
# 二分法
l,r= 1,2*n*2
while l<=r:
  mid = (l+r)//2
  if check(mid):
    ans = mid 
    l = mid+1
  else:
    r = mid-1
print(ans)
