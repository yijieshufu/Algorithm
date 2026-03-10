# 题目描述
### 问题描述

小蓝要为蓝桥画一个图形。由于小蓝的画图能力有限，他准备用大写字母 $Q$ 画一个 $L$ 形状的字符画。  
他希望 $L$ 的粗细正好是 $w$ 个字符宽，竖的笔划伸出 $h$ 高（因此图形总共 $h + w$ 高），横的笔划伸出 $v$ 宽（因此图形总共 $v + w$ 宽），要求每个笔划方方正正不能有多余内容。  
例如，当 $w = 2, h = 3, v = 4$ 时，图形如下所示：
```Plaintext
QQ
QQ
QQ
QQQQQQ
QQQQQQ
```
给定 $w, h, v$，请帮助小蓝画出这个图形。
# 代码
```python
import sys
# 请在此输入您的代码
it = iter(sys.stdin.read().split())
w=int(next(it))
h=int(next(it))
v=int(next(it))
for _ in range(h):
  print('Q' * w)
for _ in range(w):
  print('Q' * (w + v))
```