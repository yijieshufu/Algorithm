import sys
# 数据读入
it = iter(sys.stdin.read().split())
n = int(next(it))
k = int(next(it))
a = [int(next(it)) for _ in range(n)]
# check h函数
def check(mid):
    for state in range(k):
        surplus = 0
        for i in range(state,n,k):
            surplus += a[i]-mid
            if surplus<0:
                return False
    return True
l,r=0,10**14
ans = 0
while l<=r:
    mid = (l+r)//2
    if check(mid):
        ans = mid 
        l = mid+1
    else:
        r = mid-1
print(ans)