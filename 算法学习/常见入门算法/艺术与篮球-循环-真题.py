import datetime
date01 = datetime.date(2000, 1, 1) # 转化为2000-01-01的形式
date02 = datetime.date(2024, 4, 13) 
day = datetime.timedelta(days=1) # 天数加一
x = [13, 1, 2, 3, 5, 4, 4, 2, 2, 2]
c = 0
while date01 <= date02:
    date = map(int, list(str(date01).replace('-', '')))
    ans = 0
    for i in date:
        ans += x[i]
    if ans > 50:
        c += 1
    date01 += day
print(c)
