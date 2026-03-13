
### 一、 题目条件详细描述

1. **初始状态**：你手里有一排数字，从 $1$ 到 $n$ 按顺序排好（例如 $n=5$，就是 `1, 2, 3, 4, 5`）。
    
2. **核心任务**：给你 $m$ 条指令，每条指令包含两个数 $l$ 和 $r$。
    
3. **操作动作**：你需要把从第 $l$ 个位置到第 $r$ 个位置的这一段数字**当场“调头”**（翻转顺序）。
    
4. **数据规模**：$n$ 和 $m$ 最高都是 $10^5$（10万）。
    
    - **痛点**：如果你用普通的列表（Array）去做，每次翻转可能要移动 10 万个元素，做 10 万次。总计算量就是 $10^{10}$（100 亿次），这在计算机上会跑好几分钟，而题目通常只给 1-2 秒。

---

### 二、 判断题型

这道题属于 **“动态序列维护”**，具体考点是**区间翻转**。

- **判断标准**：只要看到“大规模数据”、“频繁区间修改（尤其是翻转、移动）”，普通数组（Array）就力不从心了。
    
- **必杀技**：我们需要一种能像“切香肠”一样切开、翻转、再粘回去的数据结构。最适合这种操作的是**带懒标记（Lazy Tag）的平衡树**（如 **Splay** 或 **FHQ Treap**）。

---

### 三、 解题思路

#### 1. 解决了什么痛点？

普通数组像是一串死死焊在一起的铁链，想翻转中间一段，得把铁环一个个拆了重焊。

而平衡树（以 **FHQ Treap** 为例）像是一串**带搭扣的珍珠项链**。

#### 2. 核心思路：分裂与合并

- **分裂 (Split)**：当我们要翻转 $[l, r]$ 时，我们把项链从 $l-1$ 后面解开，再从 $r$ 后面解开。这样项链就变成了三段：`左边`、`中间[l, r]`、`右边`。
    
- **懒标记 (Lazy Tag) —— 核心中的核心**：
    
    - 我们不需要真的去调换中间这段项链里每一颗珠子的位置。
        
    - 我们只需要在中间这段的“总开关”（根节点）上贴个**小纸条**：“这一段需要翻转”。
        
    - 只有当我们下次真的要经过这颗珠子时，才顺手把它的左右孩子换一下，并把纸条传给孩子。这就叫“**懒政思想**”——不到万不得已，绝不干活。
        
- **合并 (Merge)**：把三段项链按原顺序重新扣上。

---

## 代码

```python
import sys, random
sys.setrecursionlimit(200000)

input = sys.stdin.read().split()
it = iter(input)

n, m = int(next(it)), int(next(it))

# ls/rs: 左右儿子, sz: 子树大小, val: 节点值, rnd: 优先级, tag: 翻转标记
ls, rs, sz, tag = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
val = [i for i in range(n+1)]
rnd = [random.random() for _ in range(n+1)]

for i in range(1, n+1): sz[i] = 1

def up(u):
    sz[u] = sz[ls[u]] + sz[rs[u]] + 1

def down(u):
    if u and tag[u]:
        ls[u], rs[u] = rs[u], ls[u]
        if ls[u]: tag[ls[u]] ^= 1
        if rs[u]: tag[rs[u]] ^= 1
        tag[u] = 0

def split(u, k):
    if not u: return 0, 0
    down(u)
    if sz[ls[u]] >= k:
        l, r = split(ls[u], k)
        ls[u] = r; up(u)
        return l, u
    else:
        l, r = split(rs[u], k - sz[ls[u]] - 1)
        rs[u] = l; up(u)
        return u, r

def merge(u, v):
    if not u or not v: return u + v
    down(u); down(v)
    if rnd[u] < rnd[v]:
        rs[u] = merge(rs[u], v); up(u)
        return u
    else:
        ls[v] = merge(u, ls[v]); up(v)
        return v

root = 0
for i in range(1, n+1): root = merge(root, i)

for _ in range(m):
    L, R = int(next(it)), int(next(it))
    t1, t3 = split(root, R)
    t1, t2 = split(t1, L-1)
    if t2: tag[t2] ^= 1
    root = merge(merge(t1, t2), t3)

ans = []
def get_ans(u):
    if not u: return
    down(u)
    get_ans(ls[u])
    ans.append(str(val[u]))
    get_ans(rs[u])

get_ans(root)
sys.stdout.write(" ".join(ans) + "\n")
```
