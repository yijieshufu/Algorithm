import sys
it = iter(sys.stdin.read().split())
s1 = next(it)
s2 = next(it)
n = len(s1)
L,R=-1,-1 # 定位L，R L第一个，R最后一个
for i in range(n):
  if s1[i]=='#' or s2[i]=='#':
    if L ==-1:L=i
    R = i 
if L == -1:print(0);sys.exit()# 特殊 情况 无
f0 = 0 if s1[L] == '#' else 1 # 初始 新增数 f0，f1  如果f1的L列没有 要花费一个补充
f1 = 0 if s2[L] == '#' else 1
for i in range(L+1,R+1): # 开始走L+1 到R列：
  c0 = 1 if s1[i]=='.' else 0 # 两个 都是遇到 . 直接 安装
  c1 = 1 if s2[i]=='.' else 0
  p0,p1=f0,f1 # 预存上个状态
  f0 = min(p0+c0,p1+c1+c0) # 计算 f0，f1 到底当前的最小花费
  f1 = min(p1+c1,p0+c0+c1)
  if s1[i] == '#' and s2[i]=='#': # 如果 当前有 则取f0，f1的最小
    f0=f1=min(f0,f1)
print(min(f0,f1)) # 输出两个的最小
