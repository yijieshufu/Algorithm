import sys
# [块 1: 高效读取]
it = iter(sys.stdin.read().split())
s = next(it)
# [块 2: 映射计数]
cnt = [0] * 26
for char in s:
    cnt[ord(char) - 65] += 1  # 65 是 'A' 的 ASCII
# [块 3: 提取结果]
mx = max(cnt)
ans = []
for i in range(26):
    if cnt[i] == mx:
        ans.append(chr(i + 65)) # chr该数字对应的字符串
print("".join(ans)) 