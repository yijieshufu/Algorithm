# 排列问题
- **核心动作**：在 $1 \le n \le 8$ 的极小数据下，按**字典序**穷举并输出 $1 \sim n$ 的所有全排列。
- **数据边界**：$n$ 最大仅为 8，全排列总数 $8! = 40,320$，计算量在 $10^5$ 级，Python 可在 1s 内轻松完成。
# 分析
全排列必用 DFS，从小到大枚举保序，递归归来务必“恢复现场”（`st[i]=False`）。
## 代码
```python
import sys
it = iter(sys.stdin.read().strip())
n = int(next(it))
path = []           
used = [False] * (n + 1) 
def dfs():
    # 第一步：判定边界 (填够了 n 个数)
    if len(path) == n:
        print(*(path))
        return

    # 第二步：寻找选项 (尝试填入数字 i)
    for i in range(1, n + 1):
        if not used[i]:
            # 第三步：做选择
            used[i] = True
            path.append(i)   # 塞进口袋
            dfs()            # 递归向下
            # 第四步：回溯撤销 (原路返回)
            path.pop()       # 从口袋掏出来
            used[i] = False  # 标记为没用过
dfs()
```
