# --- 暴力 $O(k^2)$ ---
for j in range(1, k + 1):
    for x in range(1, j + 1): # 每次都从 1 重新加到 j
        g[j] = (g[j] + f[x]) % M

# --- 优化 $O(k)$ ---
s = 0
for j in range(1, k + 1):
    s = (s + f[j]) % M  # 桶里一直累加，不倒掉
    g[j] = s            # 现在的桶里正好就是 1 到 j 的总和
