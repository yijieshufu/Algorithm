import math
ans = 0
for i in range(1, 2022):
    if math.gcd(i, 2021) > 1:
        ans += 1
print(ans)
