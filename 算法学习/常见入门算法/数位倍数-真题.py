import sys
# 虽然是填空题，我们也写出规范的逻辑
res = 0
limit = 202504

# 外层循环用 i
for i in range(1, limit + 1):
	digit_sum = 0
	temp = i
	# 核心：数学拆解法，避免了 str() 的性能开销
	while temp > 0:
		digit_sum += temp % 10  # 拿到当前个位数
		temp //= 10             # 去掉已经拿走的个位数
		
	if digit_sum % 5 == 0:
		res += 1		
print(res)
