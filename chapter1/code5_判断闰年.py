while True:
    try:
        year = input("请输入年份(输入end退出程序): \n")
        if year == "end":
            break
        year = int(year)
        if (not year % 4 and year % 100) or (not year % 400):
            print('闰年')
        else:
            print('非闰年')
    except ValueError:
        print("请输入数字！")
# input使用
