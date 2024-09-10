# 输入日期计算，该日期是这一年的多少天？

# 定义闰年,非闰年,12月天数
mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = input('请输入日期(yyyy-MM-dd)：').split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])
result = 0

# 先判断今年是不是闰年
if (not year % 4 and year % 100) or (not year % 400):
    mDays[2] += 1

for i in range(month):
    result += mDays[i]
result += day
print(f"{year}年{month}月{day}日 在 {year} 年是第{result}天")
