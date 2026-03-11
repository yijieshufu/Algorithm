import sys 
moth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 天数
sum_days = 0
w = 6 # 从星期六开始
for i in range(12):
	for day in range(1, moth[i] + 1):
		if w == 6 or w == 0 or day in [1, 11, 21, 31]:
			sum_days += 1
		w = (w + 1) % 7 # 计算下一天的星期
print(sum_days)
