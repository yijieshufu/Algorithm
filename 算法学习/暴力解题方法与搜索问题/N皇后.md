# 题目描述
### 题目转述与约束

- **核心任务**：在一个 $N \times N$ 的棋盘上放置 $N$ 个皇后。
    
- **冲突规则**：皇后们非常“霸道”，任何两个皇后都不能处于**同一行**、**同一列**，或者**同一条 45 度斜线**（包括正斜线和反斜线）上。
    
- **目标**：输入一个正整数 $N$（$N \le 10$），求出一共有多少种不打架的摆放方法。
    
- **时空限制**：1秒运行时间，128MB 内存。

# 代码
```python
import sys
it = iter(sys.stdin.read().split())
N = int(next(it))
col = [False]*30
gd = [False]*30
udg = [False]*30
ans = 0
def dfs(u):
  global ans
  if u == N:
    ans+=1
    return
  for i in range(N): 
    if not col[i] and not gd[u+i] and not udg[u-i+N]: # 正对角线 u+i 和 反对角线u-i+n是定值
      col[i]=gd[u+i]=udg[u-i+N]=True
      dfs(u+1)
      col[i]=gd[u+i]=udg[u-i+N]=False
dfs(0)
print(ans)
```